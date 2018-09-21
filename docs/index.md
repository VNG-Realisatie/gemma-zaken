---
title: Read me
layout: default
---

# Setup Jekyll
```bash
bundle update
bundle exec jekyll serve
```

# Changes/Remarks
{% raw %} {{< relref "" >}} needs to be changed to {{ site.baseurl }}{% link "page_path" %} {% endraw %}

For link tag info: https://jekyllrb.com/docs/liquid/tags/#links

Tables: https://kramdown.gettalong.org/syntax.html#tables

## Static files
Static files now reside within assets folder (Jekylls static folder).

## Navigation
Navigation order is determined by the lowest weight value within the collection subfolder.

Pages within page collection can be part of the navigation with the following front matter added:

```
---
title: My Page Title
parent: "" # name of sub collection navigation header
weight: 10 # order in navigation list
---

your content here.
```
The lowest weight value in a markdown of each parent determines the order of parent navigation

## Redirect
For redirection use:
```
---
title: My Redirect Page
redirect_from:
  - /folder/
---
```

> more info https://www.rubydoc.info/gems/jekyll-redirect-from/0.14.0
