# Quick Match Results Feature Guide

## Overview

The Quick Match Results feature provides a mobile-friendly way to record match outcomes efficiently, especially when tracking multiple matches for a single player.

## Benefits

- Mobile-first design with large touch targets
- Default player selection via URL parameter or button grid
- Quick one-tap outcome recording
- Recent match history visible on the same page with player highlighting

## How to Use

### Accessing the Quick Match Page

1. Navigate to a tournament's match results page
2. Click the "Quick Match Entry" button
3. From player details, use the "Quick Match" dropdown
4. Or navigate directly to: `/standing/<standing_id>/quick-match-results/`

### Setting Up a Default Player

You can select your default player in two ways:

1. **From the selection screen:** When you first visit the page without a player parameter, you'll see a grid of player buttons. Simply tap the player you want to use.

2. **Using a URL parameter:** Add a player_id to the URL for bookmarking or direct access:
   - `/standing/<standing_id>/quick-match-results/?player_id=<player_id>`

Example links for existing data:
- [Quick Match for Standing 1, Player Louis (ID: 3)](/standing/1/quick-match-results/?player_id=3)
- [Quick Match for Standing 2, Player Elbert (ID: 4)](/standing/2/quick-match-results/?player_id=4)

### Recording Match Results

1. Select your opponent from the dropdown menu
2. Tap one of the outcome buttons:
   - **[Player] Won** - Your default player won the match
   - **Opponent Won** - Your opponent won the match
   - **Double Loss** - Both players receive a loss (special case)
3. The match is saved and you stay on the same page to quickly record more matches

### Viewing Match History

Recent matches appear at the bottom of the page with a visual display of the outcome:
- Regular wins show a trophy icon between players
- Double losses show an X icon between players

Matches involving your default player are highlighted with a blue border for easy identification.

For the complete match history, click "View All Matches" at the bottom.

## Tips

- Bookmark personalized quick match URLs for your most common players
- Use the player detail page's "Quick Match" button for frequently used players
- For multi-day tournaments, keep the browser tab open for faster entries
- Use this feature on phones or tablets while walking around a tournament venue

## Technical Notes

- The default player and standing are passed via query parameters for convenience
- No need to select the same player repeatedly for consecutive matches
- Matches are added to the same database as those from the standard form
