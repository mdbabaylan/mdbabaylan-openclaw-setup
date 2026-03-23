# Custom Inference API Details for Nous Models

## Endpoint Pattern

```
custom-inference-api-nousresearch-com/<MODEL_NAME>
```

## Model Name Mapping

The custom endpoint uses slightly different model naming than OpenRouter:

| OpenRouter Format (broken) | Custom API Format (working) |
|---------------------------|----------------------------|
| `nousresearch/hermes-3-llama-3.1-405b` | `Hermes-3-Llama-3.1-405B` |
| `nousresearch/hermes-4-405b` | `Hermes-4-405B` |

Note: The custom API uses PascalCase with exact version strings.

## Usage Example

```bash
# Session status with custom Nous model
openclaw session_status --model custom-inference-api-nousresearch-com/Hermes-3-Llama-3.1-405B

# Or set as default
openclaw config set default_model custom-inference-api-nousresearch-com/Hermes-3-Llama-3.1-405B
```

## Troubleshooting

- **Model not found**: Ensure you're using the exact PascalCase name from the table above
- **API errors**: The custom endpoint may have different rate limits or auth requirements than OpenRouter
- **Fallback**: If custom endpoint fails, the system should fall back to default_model
