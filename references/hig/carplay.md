# CarPlay
_CarPlay lets people get directions, make calls, send and receive messages, listen to music, and more from their car’s built-in display, all while staying focused on the road._
Source: https://developer.apple.com/design/human-interface-guidelines/carplay
> Note: CarPlay audio and video apps also work on Apple HomeView without requiring you to make any modifications to your app.

### iPhone interactions
- **Eliminate app interactions on iPhone when CarPlay is active.** Interactions with your app need to occur using the car’s built-in controls and display. If your app requires setup on iPhone, make sure people perform it before the vehicle is in motion.
- **Never lock people out of CarPlay because the connected iPhone requires input.** Your app needs to function when iPhone is inaccessible — for example, when people put it in a bag or in the trunk while driving. If people must resolve a problem on the connected iPhone, let them do so after the vehicle stops.
- **Make sure your app works without requiring people to unlock iPhone.** Most people use CarPlay while their iPhone is locked, so ensure that the features you provide in your CarPlay app work as expected in this scenario.

#### Audio
- **Let people choose when to start playback.** In general, avoid beginning playback automatically unless your app’s purpose is to play a single source of audio, or your app is resuming previously interrupted audio. Also, avoid starting an audio session until you’re ready to actually play audio because starting a session silences other audio sources, like the car’s built-in radio.
- **Start playback as soon as audio has sufficiently loaded.** After people make a selection, it may take several seconds for audio to begin playing, depending on buffering and network conditions. The system keeps the selection highlighted and displays a spinning activity indicator until your app signals that the audio is ready to play.
- **Display the Now Playing screen when audio is ready to play.** Don’t delay playback until descriptive information completes loading. If necessary, continue loading such information in the background, and show it when it’s available.
- **Resume audio playback after an interruption only when it’s appropriate.** For example, your app can resume audio after a temporary interruption like a phone call. Permanent interruptions, such as a music playlist initiated by Siri, are nonresumable. When a resumable interruption occurs, your app needs to resume playback when the interruption ends if audio was actively playing when the interruption started.
- **When necessary, automatically adjust audio levels, but don’t change the overall volume.** Although your app can adjust relative, independent volume levels to achieve a great mix of audio, people need to control the final output volume.

### Layout

| Dimensions (pixels) | Aspect ratio |
|---|---|
| 800x480 | 5:3 |
| 960x540 | 16:9 |
| 1280x720 | 16:9 |
| 1920x720 | 8:3 |

- **Provide useful, high-value information in a clean layout that’s easy to scan from the driver’s seat.** Don’t clutter the screen with nonessential details and unnecessary visual embellishments.
- **Maintain an overall consistent appearance throughout your app.** In general, ensure that elements with similar functions look similar.
- **Ensure that primary content stands out and feels actionable.** Large items tend to appear more important than smaller ones and are easier for people to tap. In general, place the most important content and controls in the upper half of the screen.

### Color
- **In general, prefer a limited color palette that coordinates with your app logo.** Subtle use of color is a great way to communicate your brand.
- **Avoid using the same color for interactive and noninteractive elements.** If interactive and noninteractive elements have the same color, it’s hard for people to know where to tap.
- **Test your app’s color scheme under a variety of lighting conditions in an actual car.** Lighting varies significantly based on time of day, weather, window tinting, and more. Colors you see on your computer at design time won’t always look the same when your app is used in the real world. Consider how color brightness might affect the experience of driving at night, and how low-contrast colors can wash out in direct sunlight. If necessary, make adjustments to provide the best possible viewing experience in the majority of use cases.
- **Ensure your app looks great in both dark and light environments.** CarPlay supports both light and dark appearances, and may automatically adjust the current appearance based on lighting conditions.
- **Choose colors that help you communicate effectively with everyone.** Different people see and interpret colors differently. For guidance on using colors in ways that people appreciate, see Inclusive color.

### Icons and images
- **Supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork in your app.** The system automatically shows the correct images and scales them appropriately, based on the resolution and size of the car’s display.
- **Mirror your iPhone app icon.** A well-designed app icon works well in CarPlay and on iPhone, without the need for a second design.
- **Don’t use black for your icon’s background.** Lighten a black background or add a border so the icon doesn’t blend into the display background.

| @2x (pixels) | @3x (pixels) |
|---|---|
| 120x120 | 180x180 |


### Error handling
- **Report errors in CarPlay, not on the connected iPhone.** If you must notify people of a problem, do so clearly in CarPlay. Never direct people to pick up their iPhone to read or resolve an error.

### Platform considerations
No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.
