from cog import BasePredictor, Input, Path
import anthropic
import os # Import os module

class Predictor(BasePredictor):
    def setup(self):
        # Read API key from environment variable
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Anthropic API key not found in environment variables (ANTHROPIC_API_KEY)")
        self.client = anthropic.Anthropic(
            api_key=api_key
        )

    def predict(self, prompt: str = Input(description="User question")) -> str:
        response = self.client.messages.create(
            model="claude-3.5-sonnet",  # replace if you have claude-3.7-sonnet access
            max_tokens=1024,
            temperature=0.2,
            messages=[
                {"role": "user", "content": f"Answer the following question based on Nelson Textbook of Pediatrics knowledge:\n{prompt}"}
            ]
        )
        # Extract text from the first content block
        if response.content and isinstance(response.content, list) and hasattr(response.content[0], 'text'):
             return response.content[0].text
        # Fallback or error handling if the structure is different
        return "Error: Could not extract response text."

