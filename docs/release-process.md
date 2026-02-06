# Release Process

1. Sync skill updates into `.codex/skills`.
2. Run `./scripts/validate_skills.sh`.
3. Update `skills-manifest.yaml` versions/changelog note.
4. Commit with a release message.
5. Tag release (`git tag vX.Y.Z`).
6. Push branch and tag.
