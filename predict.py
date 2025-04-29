from cog import BasePredictor, Input, Path
import anthropic

class Predictor(BasePredictor):
    def setup(self):
        """Initialize the model once at startup."""
        self.client = anthropic.Anthropic(
            api_key="your-anthropic-api-key-here"  # Replace with os.environ.get("ANTHROPIC_API_KEY") in production
        )
        self.model_name = "claude-3-5-sonnet-20240620"  # Or use claude-3-7-sonnet if available

    def predict(self, prompt: str = Input(description="User question")) -> str:
        """Run a single prediction on the model based on the input prompt."""
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=1024,
            temperature=0.2,
            system="Answer the following question based on Nelson Textbook of Pediatrics knowledge.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract content from response
        answer = ''
        for block in response.content:
            if block.type == 'text':
                answer += block.text

        return answer
