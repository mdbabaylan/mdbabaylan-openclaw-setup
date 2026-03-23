---
name: custom-nous-models
description: Route to Nous Research models (Hermes, etc.) via custom inference API endpoints when OpenRouter doesn't support them. Use when the user wants to use Hermes-3-Llama, Hermes-4, or other Nous models and needs to bypass OpenRouter's lack of Nous support by using a custom inference API base URL.
---

# Custom Nous Models Routing

OpenRouter does not support Nous Research models directly. This skill documents how to route to them via a custom inference API endpoint.

## When to Use

- You want Hermes-3-Llama-3.1-405B or Hermes-4-405B
- OpenRouter's model list doesn't include the Nous model you need
- You have access to a custom inference API that proxies to Nous models

## How It Works

Instead of using `openrouter/` as the provider prefix, use a custom inference API endpoint:

```
# Instead of (doesn't work):
openrouter/nousresearch/hermes-3-llama-3.1-405b

# Use:
custom-inference-api-nousresearch-com/Hermes-3-Llama-3.1-405B
```

The custom endpoint handles the routing to Nous Research's models directly.

## Known Working Models

| Model | Custom Endpoint String |
|-------|----------------------|
| Hermes-3-Llama-3.1-405B | `custom-inference-api-nousresearch-com/Hermes-3-Llama-3.1-405B` |
| Hermes-4-405B | `custom-inference-api-nousresearch-com/Hermes-4-405B` |

## Configuration

No special configuration needed — the custom endpoint is handled transparently by the system when you specify the model with the `custom-inference-api-nousresearch-com/` prefix.

## Aliases

Standard model aliases can be used:
- `Hermes-3-OR` → `openrouter/nousresearch/hermes-3-llama-3.1-405b` (OpenRouter, may not work)
- `Hermes-4-70B` → `custom-inference-api-nousresearch-com/Hermes-3-Llama-3.1-405B` (Custom API)
- `Hermes-4-OR` → `openrouter/nousresearch/hermes-4-405b` (OpenRouter, may not work)

When OpenRouter support is missing, prefer the `custom-inference-api-nousresearch-com/` prefix.
