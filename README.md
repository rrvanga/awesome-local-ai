# Awesome Local AI

A curated list of tools, models, and guides for running AI **on your own hardware** — no cloud required.

Local AI is exploding (Ollama 178k⭐, Open WebUI 148k⭐) but the information is scattered across Reddit threads, vendor blogs, and buried GitHub issues. This list organizes the genuinely useful stuff by category.

## Contents

- [Runtimes & Loaders](#runtimes--loaders)
- [Models (open-weight)](#models-open-weight)
- [Frontends & UIs](#frontends--uis)
- [Quantization & Optimization](#quantization--optimization)
- [Benchmarks & Evaluation](#benchmarks--evaluation)
- [Hardware & VRAM Planning](#hardware--vram-planning)

---

## Runtimes & Loaders

Engines that actually load weights and run inference on your box.

- [llama.cpp](https://github.com/ggml-org/llama.cpp) — The reference CPU/GPU inference engine. Runs GGUF quants on everything from a Raspberry Pi to a 5090. The foundation most local stacks sit on.
- [Ollama](https://ollama.com) — The easiest on-ramp: `ollama run llama3.3` and you're off. Modelfile system, REST API, first-class GGUF support.
- [LM Studio](https://lmstudio.ai) — Desktop GUI for browsing, downloading, and chatting with GGUF models. Great for people who never want to touch a terminal.
- [vLLM](https://github.com/vllm-project/vllm) — High-throughput serving for GPUs. PagedAttention, continuous batching. Overkill for chat, essential for serving many users.
- [koboldcpp](https://github.com/LostRuins/koboldcpp) — Single-file llama.cpp wrapper focused on story/RP use cases, with its own UI.
- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) — The "AUTOMATIC1111 of LLMs" — a Gradio web UI with loaders for every major backend.
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) — Python bindings for llama.cpp. The building block if you're scripting your own stack.
- [ExLlamaV2](https://github.com/turboderp-org/exllamav2) — Fast GPTQ/EXL2 inference for NVIDIA. The speed king for quantized models.
- [mistral.rs](https://github.com/EricLBuehler/mistral.rs) — Rust inference with support for GGUF, quantized, and vision models. Blazing fast and portable.
- [MLX](https://github.com/ml-explore/mlx) — Apple Silicon-first framework. If your local AI runs on a Mac, this is the native path.
- [Candle](https://github.com/huggingface/candle) — Minimalist Rust ML framework from Hugging Face. For embedding inference into other apps.

- [LMDeploy](https://github.com/InternLM/lmdeploy) — TurboMind-accelerated serving with persistent batching; strong tokens/sec on mid-range NVIDIA cards.
- [SGLang](https://github.com/sgl-project/sglang) — Fast serving framework with RadixAttention; a vLLM alternative that often wins on throughput benchmarks.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — NVIDIA's max-performance runtime — the ceiling for tokens/sec on GeForce/RTX, at the cost of setup complexity.

- [llamafile](https://github.com/Mozilla-Ocho/llamafile) — Mozilla's single-file executable: one binary bundles a model + llama.cpp + a web UI. Runs anywhere with zero install.
- [LocalAI](https://github.com/mudler/LocalAI) — OpenAI-compatible local API that fronts many backends (llama.cpp, whisper, diffusers). Drop-in replacement for OpenAI endpoints.
- [OnnxStream](https://github.com/vitoplantamura/OnnxStream) — Runs Stable Diffusion XL on a Raspberry Pi Zero 2 by streaming weights — the extreme edge of local inference.

## Models (open-weight)

Downloadable weights with permissive-to-open licenses. Pick by your VRAM budget.

- [Qwen](https://github.com/QwenLM/Qwen) — Alibaba's family (Qwen2.5/Qwen3). Strong coding + multilingual, excellent small sizes (0.5B–72B).
- [Llama](https://github.com/meta-llama/llama-models) — Meta's Llama 3/4 line. The default baseline everyone benchmarks against.
- [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) — Open-weight reasoning model with full chain-of-thought. Distills run on consumer GPUs.
- [Mistral](https://mistral.ai) — Efficient European models (Mistral/Mixtral/Ministral). Strong quality-per-parameter.
- [Gemma](https://ai.google.dev/gemma) — Google's open models. Gemma 3 has vision; small sizes run on a phone.
- [Phi](https://github.com/microsoft/phi-4) — Microsoft's compact models. Phi-4-mini is genuinely useful on 8GB VRAM.
- [SmolLM](https://github.com/huggingface/smollm) — Tiny (135M–3B) models for edge devices and fast CPU inference.
- [OLMo](https://github.com/allenai/OLMo) — Fully open (weights + data + training code) from AI2. Great for researchers.
- [Granite](https://github.com/ibm-granite) — IBM's open enterprise models with an Apache-2.0 license.
- [Command R](https://huggingface.co/CohereForAI) — Cohere's open RAG-optimized models.

- [RWKV](https://github.com/BlinkDL/RWKV-LM) — Linear-attention (RNN-style) models — constant memory regardless of context length, friendly to CPU and low VRAM.
- [Falcon](https://huggingface.co/tiiuae) — TII's open models, Apache-2.0, once a top open leaderboard performer; still solid for fine-tuning experiments.

## Frontends & UIs

Chat interfaces that talk to the runtimes above.

- [Open WebUI](https://github.com/open-webui/open-webui) — Full-featured ChatGPT-style UI with RAG, tools, and multi-user support. The most popular local frontend.
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) — Roleplay/character-focused frontend with deep lore and prompt control.
- [Continue](https://github.com/continuedev/continue) — Open-source AI code assistant that can point at a local model instead of an API.
- [Jan](https://jan.ai) — Local-first AI app with a clean desktop UI, model hub, and API server.
- [GPT4All](https://github.com/nomic-ai/gpt4all) — Desktop client optimized for CPU-only machines. Runs on ordinary laptops.
- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) — Desktop + Docker "AI business" app: chat with your docs over a local model.
- [Msty](https://msty.app) — Local AI desktop app with side-by-side model comparisons and prompt library.

- [Faraday](https://faraday.dev) — Desktop local-AI app with a focus on offline-first chat and roleplay; batteries included, no terminal needed.

## Quantization & Optimization

Shrinking models to fit your VRAM/RAM — the difference between "can't run" and "runs great".

- [GGUF](https://github.com/ggml-org/llama.cpp/discussions) — The de-facto single-file quantized format. K-quants (Q4_K_M etc.) are the sweet spot for most GPUs.
- [Unsloth](https://github.com/unslothai/unsloth) — 2–5× faster, 80% less VRAM for fine-tuning. Also ships pre-quantized popular models.
- [GPTQ](https://github.com/AutoGPTQ/AutoGPTQ) — Post-training quantization for NVIDIA; pairs with ExLlamaV2.
- [AWQ](https://github.com/mit-han-lab/llm-awq) — Activation-aware quantization that preserves quality better at low bits.
- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) — 8-bit/4-bit quantization lib (the QLoRA backbone), now multi-backend.
- [TheBloke](https://huggingface.co/TheBloke) — The canonical source of pre-quantized GGUF/GPTQ uploads for thousands of models.

## Benchmarks & Evaluation

Measuring what actually fits and how fast it runs.

- [whichllm](https://github.com/Andyyyy64/whichllm) — Benchmark local LLMs on your own hardware; answers "what can my GPU actually run well?"
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — EleutherAI's standard harness for scoring models (MMLU, GSM8K, etc.).
- [Geekbench AI](https://www.geekbench.com/ai/) — Cross-platform AI performance scores, hardware-comparable across devices.
- [MLPerf Inference](https://mlcommons.org/benchmarks/inference-datacenter/) — The industry-standard inference benchmark suite.
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — HF's quality leaderboard, with a helper to check which models fit your GPU.
- [LMArena](https://lmarena.ai) — Crowdsourced model-vs-model arena (mostly API models, useful as a quality reference).

## Hardware & VRAM Planning

Choosing hardware and sizing models before you spend money.

- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) — The hub of local-AI builds, VRAM math, and real-world tokens/sec reports.
- [HF GPU VRAM guide](https://huggingface.co/docs/transformers/model_memory_anatomy) — How model params + quantization map to memory footprint.
- [NVIDIA consumer GPU lineup](https://www.nvidia.com/en-us/geforce/graphics-cards/) — VRAM tiers for the current generation (the 16GB vs 24GB decision matters enormously here).
- [Rule-of-thumb VRAM formula](https://github.com/ggerganov/llama.cpp/discussions/4087) — Params × bytes-per-weight × 1.2 overhead ≈ VRAM needed; the number to know before any download.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). One entry per PR is fine — quality over quantity. New entries are also dripped daily from the maintainer's backlog.

## License

[CC0-1.0](LICENSE) — this list is public domain. Steal it, remix it, ship it.
