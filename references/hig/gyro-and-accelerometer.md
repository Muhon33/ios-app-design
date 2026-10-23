# Gyroscope and accelerometer
_On-device gyroscopes and accelerometers can supply data about a device’s movement in the physical world._
Source: https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer

### Best practices
- **Use motion data only to offer a tangible benefit to people.** For example, a fitness app might use the data to provide feedback about people’s activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.
> Important: If your experience needs to access motion data from a device, you must provide copy that explains why. The first time your app or game tries to access this type of data, the system includes your copy in a permission request, where people can grant or deny access.
- **Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface.** Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

### Platform considerations
No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.
