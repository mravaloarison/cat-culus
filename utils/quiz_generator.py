from google import genai
import os, json
from pydantic import BaseModel

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class QuizGenerated(BaseModel):
    instructions: str
    combinations: list[list[int, int]]

def generate_quiz():
    prompt = """
        Generate 15 math-based quizzes that meet the following criteria:
            - Each question should involve two unknown numbers, x and y, and use all addition, subtraction, multiplication, square, cube, or other mathematical operations.
            - Don't Always use the same operation for each question.
            - Ensure x and y are always less than or equal to 5 in value.
            - The challenge should be for the user to guess x and y based on the given equation.
            - The instruction should not reveal that the numbers are less than 5.
            - Examples:
                * 'instructions': 'Find the two numbers, x and y, that satisfy the equation: x + y = 10.', 'combinations': [[5, 5]]
                -> Explanation: The only combination of x and y that satisfies the equation x + y = 10 is 5 + 5 = 10.

                * 'instructions': 'What are the two numbers, x and y, that satisfy the equation: x - y = -1?', 'combinations': [[0,1],[1,2], [2, 3], [3, 4], [4, 5]]
                -> Explanation: The combinations of x and y that satisfy the equation x - y = -1 are 0 - 1 = -1, 1 - 2 = -1, 2 - 3 = -1, 3 - 4 = -1, and 4 - 5 = -1.

                * 'Find the two numbers, x and y, that fulfill the equation: x / y = 2.', 'combinations': [[4, 2]]
                -> Explanation: The only combination of x and y that satisfies the equation x / y = 2 is 4 / 2 = 2.
                ....
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": list[QuizGenerated],
        }
    )

    array_of_keywords = json.loads(response.text)

    return array_of_keywords
