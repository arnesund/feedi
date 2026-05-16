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

### Right sidebar hidden by default, folders in left sidebar (`feedi/routes.py`, `feedi/templates/base.html`)

The right settings sidebar is now hidden on both desktop and mobile by default,
and only appears when clicking "Settings" in the left sidebar (or mobile menu).
The left sidebar also lists all feed folders (tags), with the active folder highlighted
and an open-folder icon. The folder list is restored from the `shortcut_folders` context
processor which was stripped from the template by upstream.

### Chronological sort option restored (`feedi/models.py`, `feedi/routes.py`, `feedi/templates/base.html`)

Upstream removed the chronological (recency) sorting option in commit ed65144. Restored
the two-button toggle in the settings sidebar (clock icon = chronological, calendar icon =
frequency-based). Chronological order is now the default. The toggle only appears on mixed
feed views (home page, folders), not when browsing a specific feed.

### Per-feed `use_related_link` option for RSS feeds (`feedi/models.py`, `feedi/parsers/rss.py`, `feedi/routes.py`, `feedi/templates/feed_edit.html`)

Some RSS feeds (e.g. Daring Fireball) put the linked external article as the `<link>`
and include the site's own permalink as `<link rel="related">`. When `use_related_link`
is enabled on a feed, the parser uses the related link as the entry URL instead of the
default link. Configurable per-feed via a checkbox in the feed edit form.

### Mastodon support restored (`feedi/parsers/mastodon.py`, `feedi/auth.py`, `feedi/models.py`, `feedi/routes.py`, `feedi/templates/mastodon.html`)

Upstream removed Mastodon support in v1 (commit 408068e) without explanation.
Restored the full feature: OAuth login flow, timeline and notifications feeds,
favorite and boost actions. Also restored the `MASTODON_FETCH_LIMIT` config key
that was dropped from `feedi/config/default.py` along with the v1 changes.
