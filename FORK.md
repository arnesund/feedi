# Fork of facundoolano/feedi

This is a fork of [facundoolano/feedi](https://github.com/facundoolano/feedi) with local improvements.

## Changes

### Environment variable config overrides (`feedi/app.py`)

Added `app.config.from_prefixed_env("FEEDI")` to `load_config`, so any
config key from `feedi/config/default.py` can be overridden via a
`FEEDI_<KEY>` environment variable without editing Python files.

Set overrides in `/etc/feedi.env` (already loaded by the systemd unit via
`EnvironmentFile=`). Examples:

```
FEEDI_RSS_SKIP_OLDER_THAN_DAYS=31
FEEDI_DELETE_AFTER_DAYS=31
FEEDI_ENTRY_PAGE_SIZE=20
```

### Mastodon support restored (`feedi/parsers/mastodon.py`, `feedi/auth.py`, `feedi/models.py`, `feedi/routes.py`, `feedi/templates/mastodon.html`)

Upstream removed Mastodon support in v1 (commit 408068e) without explanation.
Restored the full feature: OAuth login flow, timeline and notifications feeds,
favorite and boost actions.
