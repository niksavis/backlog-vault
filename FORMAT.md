# Vault format 1

Each writer appends to its own files under `log/WRITER/`. A line is one JSON object with
`id`, `kind`, `record`, `writer`, `session` and `at`. The first valid claim of a record, in the
order of this repository's first-parent history, holds the record.
