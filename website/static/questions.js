document.addEventListener('DOMContentLoaded', () => {
    async function fetchQuestions() {
        const response = await fetch('/get_questions');
        if (response.ok) {
            const questions = await response.json();
            const dropdown = document.getElementById('questionDropdown');
            questions.forEach(question => {
                const option = document.createElement('option');
                option.value = question.titleSlug;
                option.textContent = question.title;
                dropdown.appendChild(option);
            });
        } else {
            console.error('Failed to fetch questions');
        }
    }

    async function loadQuestion() {
        const slug = document.getElementById('questionDropdown').value;
        if (!slug) {
            alert('Please select a question');
            return;
        }
        const response = await fetch(`/get_question_details?slug=${slug}`);
        if (response.ok) {
            const question = await response.json();
            document.getElementById('questionDisplay').textContent = question.content;
        } else {
            console.error('Failed to fetch question details');
        }
    }

    document.getElementById('loadQuestion').addEventListener('click', loadQuestion);

    require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.33.0/min/vs' }});
    require(["vs/editor/editor.main"], function () {
        const editor = monaco.editor.create(document.getElementById('editor'), {
            value: "# Write your code here",
            language: "python",
            theme: "vs-dark"
        });

        document.getElementById('runCode').addEventListener('click', async () => {
            const code = editor.getValue();
            const response = await fetch('/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code })
            });
            const result = await response.json();
            document.getElementById('output').textContent = result.output || result.error;
        });
    });

    fetchQuestions();
});
