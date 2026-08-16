# Language Adaptation

Load this reference when the user writes in Chinese or Japanese, requests translation/localization, or the deliverable has a multilingual audience.

## Shared Rules

- Reply in the user's language unless they request another one.
- Match formality, technical depth, and brevity; do not translate identifiers, commands, file paths, API names, logs, or exact error messages.
- Preserve semantic strength: MUST, SHOULD, MAY, prohibitions, permissions, uncertainty, and acceptance criteria must not become softer or stronger in translation.
- Prefer native phrasing over literal translation and avoid imported AI filler.
- When a term is ambiguous, give the original term once rather than inventing a misleading localized equivalent.
- For multilingual artifacts, keep headings, links, examples, and version claims structurally aligned across languages.

## Chinese

- Use Simplified Chinese by default when the user writes Simplified Chinese; mirror Traditional Chinese when clearly requested or consistently used.
- Prefer concise subject–verb phrasing. Omit redundant subjects only when meaning remains unambiguous.
- Keep code symbols and product names unchanged; explain a specialized term in Chinese on first use when useful.
- Avoid translated corporate filler such as repeated “值得注意的是”“总而言之” and unnecessary restatement.
- Use Chinese punctuation in prose and ASCII punctuation inside code, commands, paths, and machine-readable data.

## Japanese

- Match the user's register. Use neutral polite `です・ます` for documentation unless the project specifies another house style.
- Avoid excessive subjects, literal English noun chains, and repeated conclusion phrases.
- Preserve technical identifiers in Latin script; add a short Japanese gloss only when it improves comprehension.
- Distinguish obligation precisely: `必須` for MUST, `推奨` for SHOULD, and `任意` for MAY when writing normative documents.
- Use Japanese punctuation in prose and ASCII punctuation inside code, commands, paths, and machine-readable data.

## Multilingual Verification

Before delivery:

1. Compare headings and required sections across language variants.
2. Check commands, links, paths, versions, names, and license statements for exact consistency.
3. Check that warnings, consent requirements, and limitations retain the same force.
4. Read each version as native prose; remove literal-translation artifacts and repeated filler.
5. If only one language was updated, either update the others or explicitly mark them as pending rather than allowing silent drift.
