def check_feedback(user_output, expected_output):
    """
    Compare the user output with the expected output and provide feedback.

    Args:
    - user_output (str): The output produced by the user's code.
    - expected_output (str): The correct output for comparison.

    Returns:
    - str: Feedback message indicating the correctness of the user output.
    """
    if user_output == expected_output:
        return "Correct! Your solution matches the expected output."
    elif expected_output in user_output:
        return "Close! Your output is partially correct."
    else:
        return "Incorrect. Please review your code and try again."
