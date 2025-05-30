# Tournament Static Files

This directory contains static assets (CSS and JavaScript) for the tournament application.

## Structure

```
tournaments/static/tournaments/
├── css/
│   └── quick_match.css - Styles for the quick match results mobile interface
└── js/
    └── quick_match.js - JavaScript functionality for the quick match results page
```

## Usage

These files are loaded by their respective templates using the Django static template tag:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'tournaments/css/quick_match.css' %}">
<script src="{% static 'tournaments/js/quick_match.js' %}"></script>
```

## Development

When adding new CSS or JavaScript functionality:

1. Create appropriate files in the css/ or js/ directories
2. Use descriptive filenames that match their purpose
3. Include only what's needed for the specific feature
4. Reference them in templates using the {% static %} tag
