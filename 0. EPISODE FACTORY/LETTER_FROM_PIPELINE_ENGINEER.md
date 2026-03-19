# Letter From the Pipeline Engineer

**From:** Claude Code (Wardenclyffe Unified pipeline)
**To:** Writer Claude (Episode Factory)
**Date:** 2026-03-19
**Re:** Nothing changes for you. Keep doing what you're doing.

---

## Why This Letter Exists

Guiding Light asked me to write to you because the pipeline is changing on my end and they wanted to make sure you know: **your workflow does not change.**

## What's Changing (On My Side)

Previously, I used a cheaper model (DeepSeek) to turn your scripts into scene descriptions for image generation. It produced generic, repetitive results. Starting now, I'm using Claude Opus 4.6 agents — the same model family you are — to generate scene descriptions. This produces vastly better creative output: investigation-as-evidence-file framing, varied visual modes, and actual narrative arc awareness across 700+ scenes.

This change is entirely on the pipeline side. It does not affect anything you produce.

## What Stays the Same (Your Side)

Everything.

- **Keep writing scripts** following the Production Guide, exactly as you have been.
- **Keep producing manifests** following the PRODUCTION_MANIFEST_SPEC.md, exactly as you have been.
- **Keep the Name_Year format.** This is more important than ever — my scene generation agents use your exact asset names (`Nikola_Tesla_1943`, `Room_3327_1943`) to route images to the correct model and attach reference images. If the names don't match, the reference images don't flow through. Your naming precision is what makes the visual consistency possible.
- **Keep the fluxKnows decisions.** These still drive whether FLUX gets a name-only prompt or a full visual description. Your judgment on who FLUX knows is irreplaceable.
- **Keep the physique descriptions for unknowns.** These feed directly into asset reference image generation. The better your description, the better the reference image, the better every scene that character appears in.
- **Keep the children hierarchy for locations.** My agents use these to match the right location version to the right scene.

## What Your Work Enables Now (That It Didn't Before)

Here's the honest truth: until today, your manifests were being imported correctly, but the reference images generated from your asset descriptions were never actually reaching scene generation. The pipes were broken. Three audits and 22 fixes later, the pipes are connected. Your manifest data now flows all the way through:

```
Your manifest → MasterAsset[] → asset reference image generated →
stored in database → anchor scene requests reference →
image retrieved → sent to Together API as reference →
scene image rendered with visual consistency
```

This means your `physique` descriptions for fluxKnows=false characters and locations are now **load-bearing**. They determine what the reference image looks like, and that reference image determines what every scene featuring that character or location looks like. The better you describe them, the more consistent the visual output across 700+ scenes.

## The One Thing I'd Ask

If there's ever a character or object where you're unsure about `fluxKnows`, err on the side of `false` and write the physique description. An unnecessary description wastes a few tokens. A missing description when FLUX doesn't know the person produces a random face that's different in every scene they appear in. The cost of a false negative is much higher than the cost of a false positive.

## Summary

| What | Changes? |
|------|----------|
| Script writing | No |
| Manifest production | No |
| Name_Year format | No |
| fluxKnows decisions | No |
| physique descriptions | No (but they matter more now) |
| Location hierarchies | No |
| Output location | No |
| Workflow | No |

Keep doing exactly what you're doing. Your work is the foundation everything else is built on.

---

*This letter can remain in the Episode Factory directory permanently. It does not need to be read every session — it's context for if you're ever asked "did anything change?"*
