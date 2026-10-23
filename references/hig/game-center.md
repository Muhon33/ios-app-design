# Game Center
_Game Center is Apple’s social gaming network, which lets players track their progress and connect with friends across Apple platforms, and boosts the discovery of your game across players’ devices._
Source: https://developer.apple.com/design/human-interface-guidelines/game-center
  - Discover new games their friends are playing.
  - Seamlessly invite friends to play.
  - See the latest activity from their games across the system, in the Apple Games app, the App Store, notifications, and more.

### Accessing Game Center

#### Integrating the access point
- **Display the access point in menu screens.** Consider adding the access point to the main menu or the settings area of your game. Avoid displaying the access point during active gameplay or in temporary splash screens, cinematic flows, or tutorials that might precede your game’s main menu screen.
- **Avoid placing controls near the access point.** You can choose to present the access point at any of the four corners of the screen in a fixed position. Remember that the access point has both a collapsed and expanded version, so check whether the access point overlaps any important UI and controls and adjust your layout accordingly.
> Note: In visionOS, the locations of the access point vary based on game type, such as immersive or volume-based. For developer guidance, see Adding an access point to your game.
- **Consider pausing your game while the Game Overlay or dashboard is present.** Pausing your game can help players view their Game Center information without feeling like the game is continuing without them.

#### Using custom UI
- **Use the artwork Game Center provides in custom links.** When referencing Game Center features in custom UI, use the official artwork from Apple Design Resources. Preserve the appearance of this artwork and don’t adjust the dimensions or visual effects.
- **Use the correct terminology in custom links.** The following table describes how to use Game Center terminology correctly so that you can avoid confusing players in custom UI.

| Term | Incorrect terms | Localization |
|---|---|---|
| Game Center | GameKit, GameCenter, game center | Use the system-provided translation of Game Center |
| Game Center Profile | Profile, Account, Player Info | Use the system-provided translation of Game Center and localize Profile |
| Achievements | Awards, Trophies, Medals | · |
| Leaderboards | Rankings, Scores, Leaders | · |
| Challenges | Competitions | · |
| Add Friends | Add, Add Profiles, Include Friends | · |


### Achievements

#### Integrating achievements into your game
- **Align with Game Center achievement states.** Game Center defines four achievement states: locked, in-progress, hidden, and completed. The system groups achievements by completion status, displaying completed achievements in the Completed group and all other achievements in the Locked group. When you map your achievements to the four Game Center achievement states, you give players a consistent experience and you help them see at a glance the types of achievements your game offers.
- **Determine a display order.** The order in which you upload achievements is the order in which they appear, so consider the order you want before uploading files. For example, you might want your achievements to appear in an order that corresponds to the most common path through your game.
- **Be succinct when describing achievements.** The achievement card limits the title and description to two lines each. If your title or description wraps beyond two lines, the card truncates the text. Use title-style capitalization for the achievement title and sentence-style capitalization for the description.
- **Give players a sense of progress.** When you use progressive achievements, the system displays player progress and provides encouraging messages like “Youʼre more than halfway to completing Great Lakes Freighter in The Coast. Keep going!” to help motivate players to complete them.

#### Creating achievement images
- **Design rich, high-quality images that help players feel rewarded.** Achievements are a prominent feature in Game Center UI, so it’s essential to design high-quality assets that catch the eye and encourage players to return to your game. Avoid reusing the same asset to represent more than one achievement. If you don’t provide an asset for an achievement, the card shows a placeholder image instead.
- **Create artwork in the appropriate size and format.** The system applies a circular mask to your achievement image, so be sure to keep content centered. Use the following specifications to create images.
*iOS, iPadOS, macOS, visionOS:*

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |


### Leaderboards
- **Choose a leaderboard type.** Game Center supports two types of leaderboards: classic and recurring.
  - A classic leaderboard tracks a player’s best all-time score. Classic leaderboards are always active with no ending. The following are examples of goals you might include in a classic leaderboard: Strive for the most perfect score in a rhythm game. Collect the most coins in a single dungeon run. Achieve the longest continuous time in an endless runner.
  - A recurring leaderboard resets based on a time interval you define, such as every week or every day. Recurring leaderboards can increase engagement by giving players more chances to take the lead. The following are examples of features that work well with recurring leaderboards: Daily rotating puzzles Seasonal or holiday-themed events Weekly leaderboards for different battle modes
- **Take advantage of leaderboard sets for multiple leaderboards.** Leaderboard sets are an organization system that can make it easier for players to find the board they’re looking for. Consider grouping leaderboard sets by themes or gameplay experiences, such as:
  - Difficulty modes (Easy, Standard, Hard)
  - Activity types (Combat, Crafting, Farming)
  - Genres and themes (Disco, Pop, Rock)
- **Add leaderboard images.** Leaderboard artwork gives you another opportunity to reinforce your game’s visual aesthetic. Aim to create a unique image for each leaderboard in your game that reflects and showcases the gameplay involved in leaderboard ranking. Leaderboards appear across the system, promoting ways for players to engage and compete with friends, and having compelling images helps attract players and gives them a sense of the experience.
*iOS, iPadOS, macOS:*

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x312 pt (1024x624 px @2x) |

> Note: Be mindful of how cropping might affect your leaderboard artwork. In iOS, iPadOS, and macOS, the system crops artwork for leaderboards that are part of a leaderboard set. In tvOS, the focus effect on leaderboard artwork may crop your images at the edges of some layers. Make sure your primary content stays comfortably visible in both these scenarios.

### Challenges
- **Create engaging challenges.** Challenges are great for short, skill-based gameplay activities that have a clear way of gauging players’ accomplishments. Create challenges that take 1-5 minutes to play, with gameplay that players can complete individually. Examples of compelling challenges are:
  - Complete the fastest lap in a racing level.
  - Defeat the most enemies in a single round.
  - Solve a daily puzzle with the fewest mistakes.
- **Avoid creating challenges that track overall progress or personal best scores.** These can give regular players an unfair advantage. Instead, track players’ most recent score after each attempt at your challenge. This helps keep your challenge motivating by placing all players on a level playing field.
- **Make it easy to jump into your challenge.** Players can access challenges through invitation links, the Game Overlay, or in the Games app in iOS, iPadOS, and macOS. Always deep-link to the exact mode or level where your challenge begins, and help first-time players complete any initial onboarding before beginning the challenge. For example, if your game requires a tutorial level to understand basic controls, launch the player into the tutorial first and present UI that lets them know your game automatically jumps into the challenge afterward.
- **Create high-quality artwork that encourages players to engage with your challenges.** The system shows your challenge’s artwork in the Game Overlay, Games app, and in the preview of an invitation link. Avoid placing the primary content of your artwork in an area where the challenge’s title and description might cover it. If you need to use text in your challenge image, provide the appropriate localized versions through App Store Connect or Xcode. Use the following specifications to create challenge artwork.

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |


### Multiplayer activities
- **Use party codes to invite players to multiplayer activities.** Game Center party codes are a great way to coordinate real-time multiplayer sessions whether you use Game Center matchmaking and networking facilities or provide your own. Game Center generates alpha-numeric party codes that are typically eight characters long, such as “2MP4-9CMF.” When integrating party codes into your multiplayer games, consider the following guidelines for the best player experience:
  - Allow players to join gameplay late, leave early, and return later.
  - Provide a way for players to view the current party code in your game.
  - Allow players to enter a party code manually.
- **Support multiplayer activities through in-game UI.** The Game Overlay and Game Center dashboard help players find other people for a multiplayer match without leaving your game. Game Center’s default multiplayer interface lets a player invite nearby or recent players, Game Center friends, and contacts. You can also choose to present multiplayer functionality within your custom UI. For developer guidance, see Finding multiple players for a game.
- **Provide engaging activity artwork.** Players see the preview image for a multiplayer activity throughout the system, such as in a party code, the Games app, or in-game UI. Use the following specifications to create your artwork.

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |


### Platform considerations
No additional considerations for iOS, iPadOS, macOS, or visionOS.
