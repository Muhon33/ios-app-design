# Action button
_The Action button gives people quick access to their favorite features on supported iPhone and Apple Watch models._
Source: https://developer.apple.com/design/human-interface-guidelines/action-button

### Best practices
- **Support the Action button with a set of your app’s essential functions.** For example, if your cooking app includes an egg timer, a “Start Egg Timer” action might be one that people want to initiate when they press the Action button. You don’t need to offer an App Shortcut that opens your app, because the system provides this function already. Your app icon, widgets, and Apple Watch complications give people other quick ways to open your app. For additional guidance, see App Shortcuts.
- **For each action you support, write a short label that succinctly describes it.** People see your labels when they visit Settings to configure the Action button’s behavior. Create labels that use title-style capitalization, begin with a verb, use present tense, and exclude articles and prepositions. Keep labels as short as possible, with a maximum of three words. For example, use “Start Race” instead of “Started Race” or “Start the Race.”
- **Prefer letting the system show people how to use the Action button with your app.** When you support the Action button, the system automatically helps people configure it to initiate one of your app’s functions. Avoid creating content that repeats the guidance offered in Settings for the Action button, or other usage tips the system provides.

### Platform considerations
Not supported in iPadOS, macOS, tvOS, or visionOS.

#### iOS
- **Let people use your actions without leaving their current context.** When possible, make use of lightweight multitasking capabilities like Live Activities and custom snippets to provide functionality without opening your app. For example, the “Set Timer” action doesn’t launch the Clock app; it prompts people to set a duration for the timer, and then launches a Live Activity with the countdown.
