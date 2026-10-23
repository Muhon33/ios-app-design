# Playing haptics
_Playing haptics can engage people’s sense of touch and bring their familiarity with the physical world into your app or game._
Source: https://developer.apple.com/design/human-interface-guidelines/playing-haptics
  - In an iPadOS, macOS, tvOS, or visionOS app or game, game controllers can provide haptic feedback (for developer guidance, see Playing Haptics on Game Controllers).
  - Apple Pencil Pro and some trackpads can provide haptic feedback when connected to certain iPad models. (For details on Apple Pencil features and compatibility, see Apple Pencil.)

### Best practices
- **Use system-provided haptic patterns according to their documented meanings.** People recognize standard haptics because the system plays them consistently on interactions with standard controls. If the documented use case for a pattern doesn’t make sense in your app or game, avoid using the pattern to mean something else. Instead, use a generic pattern or create your own, where supported. For guidance, see Custom haptics.
- **Use haptics consistently throughout your app or game.** It’s important to build a clear, causal relationship between each haptic and the action that causes it so people learn to associate certain haptic patterns with certain experiences. If a haptic doesn’t reinforce a cause-and-effect relationship, it can be confusing and seem gratuitous. For example, if your game plays a specific haptic pattern when a character fails to finish a mission, people associate that pattern with a negative outcome. If you use the same haptic pattern for a positive outcome like a level completion, people will be confused.
- **Prefer using haptics to complement other feedback in your app or game.** When visual, auditory, and tactile feedback are in harmony — as they generally are in the physical world — the user experience is more coherent and can seem more natural. For example, you generally want to match the intensity and sharpness of a haptic with the intensity and sharpness of the animation it accompanies. You can also synchronize sound with haptics; for developer guidance, see Delivering Rich App Experiences with Haptics.
- **Avoid overusing haptics.** Sometimes a haptic can feel just right when it happens occasionally, but become tiresome when it plays frequently. Doing user testing can help you discover a balance that most people appreciate. Often, the best haptic experience is one that people may not be conscious of, but miss when it’s turned off.
- **In most apps, prefer playing short haptics that complement discrete events.** Although long-running haptics that accompany a gameplay flow can enhance the experience, long-running haptics in an app can dilute the meaning of the feedback and distract people from their task. On Apple Pencil Pro, for example, continuous or long-lasting haptics don’t tend to clarify the writing or drawing experience and can even make holding the pencil less pleasant.
- **Make haptics optional.** Let people turn off or mute haptics, and make sure people can still enjoy your app or game without them.
- **Be aware that playing haptics might impact other user experiences.** By design, haptics produce enough physical force for people to feel the vibration. Ensure that haptic vibrations don’t disrupt experiences involving device features like the camera, gyroscope, or microphone.

### Custom haptics
  - Transient events are brief and compact, often feeling like taps or impulses. The experience of tapping the Flashlight button on the Home Screen is an example of a transient event.
  - Continuous events feel like sustained vibrations, such as the experience of the lasers effect in a message.

### Platform considerations

#### iOS
On supported iPhone models, you can add haptics to your experience in the following ways:
  - Use standard UI components — like toggles, sliders, and pickers — that play Apple-designed system haptics by default.
  - When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of notification, impact, and selection (for developer guidance, see UIFeedbackGenerator).

##### Notification
Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

##### Impact
Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.

##### Selection
Selection haptics provide feedback while the values of a UI element are changing.
