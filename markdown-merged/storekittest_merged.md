# storekittest

*Merged documentation for storekittest*

---

# StoreKit Test

## 

The StoreKitTest framework makes StoreKit testing in Xcode available for automation. Use this framework to write unit tests and continuous integration tests. Use [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession) and [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession) to control the test environment.

For testing in-app purchase transactions, use `SKTestSession`. Each instance of `SKTestSession` gives you access to the same settings you manually change for StoreKit testing in Xcode. Use this class to test a variety of in-app purchase scenarios, such as subscription renewals and Ask to Buy transactions, and maintain control over the transactions in the testing environment.

For testing ad impressions and postbacks, use `SKAdTestSession`. Each instance of `SKAdTestSession` holds a set of test postbacks that you create and can use in multiple unit tests. Ad networks that use [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork) APIs can use this class to validate the ad impressions that they sign, and test receiving postbacks on their server. Advertised apps can test their conversion value updates.

Testing StoreKit in iOS, watchOS, or tvOS apps requires Xcode 12 or later running on macOS 10.15 or later. Testing StoreKit in a macOS app requires Xcode 12 or later running on macOS 11 or later.

> **NOTE:** Session 10659 : [https://developer.apple.com/wwdc20/10659](https://developer.apple.com/wwdc20/10659)

## Topics

### StoreKit transaction testing

- [setting-up-storekit-testing-in-xcode](../com.apple.Xcode/setting-up-storekit-testing-in-xcode.md)
- [SKTestSession](../com.apple.storekittest/StoreKitTest/SKTestSession.md)
- [SKTestTransaction](../com.apple.storekittest/StoreKitTest/SKTestTransaction.md)

### StoreKit transaction testing errors

- [SKTestErrorDomain](../com.apple.storekittest/StoreKitTest/SKTestErrorDomain.md)
- [SKTestError](../com.apple.storekittest/StoreKitTest/SKTestError.md)

### Ad impression and postback testing

- [testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork](../com.apple.storekittest/StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
- [SKAdTestSession](../com.apple.storekittest/StoreKitTest/SKAdTestSession.md)
- [SKAdTestPostback](../com.apple.storekittest/StoreKitTest/SKAdTestPostback.md)
- [SKAdTestPostbackResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse.md)
- [SKAdTestPostbackVersion](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion.md)

### Ad impression and postback errors

- [SKAdTestErrorDomain](../com.apple.storekittest/StoreKitTest/SKAdTestErrorDomain.md)
- [SKAdTestError](../com.apple.storekittest/StoreKitTest/SKAdTestError.md)

### Structures

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

### Enumerations

- [SKTestFailures](../com.apple.storekittest/StoreKitTest/SKTestFailures.md)

### Protocols

- [FailableStoreKitAPI](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI.md)
- [SKTestFailure](../com.apple.storekittest/StoreKitTest/SKTestFailure.md)

---


# Detailed Documentation


## SKTestError


### Code

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum Code
```

## Topics

### Error Codes

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/Code/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/Code/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/Code/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/Code/serviceUnavailable.md)
- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/Code/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/Code/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/Code/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/Code/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/Code/serviceUnavailable.md)

### Initializers

- [init(rawValue:)](../com.apple.storekittest/StoreKitTest/SKTestError/Code/init(rawValue:).md)

---


### errorDomain

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var errorDomain: String { get }
```

---


### fileNotFound

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var fileNotFound: SKTestError.Code { get }
```

## See Also

- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### invalidAction

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var invalidAction: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### invalidProductIdentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var invalidProductIdentifier: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### invalidProductType

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var invalidProductType: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### invalidURL

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var invalidURL: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### noSubscriptionFound

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var noSubscriptionFound: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### noTransactionFound

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var noTransactionFound: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


### serviceUnavailable

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
static var serviceUnavailable: SKTestError.Code { get }
```

## See Also

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

---


## SKTestSession


### TimeRate-swift.enum


#### fiveMinutesIsOneDay

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
case fiveMinutesIsOneDay
```

## See Also

- [oneHourIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneHourIsOneDay.md)
- [thirtyMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtyMinutesIsOneDay.md)
- [oneMinuteIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneMinuteIsOneDay.md)
- [thirtySecondsIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtySecondsIsOneDay.md)
- [oneSecondIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneSecondIsOneDay.md)

---


#### init(rawValue:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
init?(rawValue: Int)
```

---


#### monthlyRenewalEveryFifteenMinutes

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case monthlyRenewalEveryFifteenMinutes
```

## 

The following table shows how this time rate affects subscriptions with various renewal periods in the testing environment:

| Subscription renewal period | Renewal time |
| --- | --- |
| Weekly | 5 minutes |
| Monthly | 15 minutes |
| Bimonthly | 30 minutes |
| Quarterly | 45 minutes |
| Semiannually | 1 hour 30 minutes |
| Annually | 3 hours |

The sandbox environment also supports this subscription renewal rate. For more information about renewal rates in the sandbox environment, see [https://help.apple.com/app-store-connect/#/dev7e89e149d](https://help.apple.com/app-store-connect/#/dev7e89e149d).

The time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 4 minutes 17 seconds |
| Grace period for subscriptions with all other renewal periods | 7 minutes 30 seconds |
| Billing retry period | 30 minutes |

## See Also

- [realTime](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime.md)
- [monthlyRenewalEveryHour](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryHour.md)
- [monthlyRenewalEveryThirtyMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtyMinutes.md)
- [monthlyRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFiveMinutes.md)
- [monthlyRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds.md)

---


#### monthlyRenewalEveryFiveMinutes

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case monthlyRenewalEveryFiveMinutes
```

## 

The following table shows how this time rate affects subscriptions with various renewal periods in the testing environment:

| Subscription renewal period | Renewal time |
| --- | --- |
| Weekly | 3 minutes |
| Monthly | 5 minutes |
| Bimonthly | 10 minutes |
| Quarterly | 15 minutes |
| Semiannually | 30 minutes |
| Annually | 1 hour |

The sandbox environment also supports this subscription renewal rate. For more information about renewal rates in the sandbox environment, see [https://help.apple.com/app-store-connect/#/dev7e89e149d](https://help.apple.com/app-store-connect/#/dev7e89e149d).

The time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 2 minutes 34 seconds |
| Grace period for subscriptions with all other renewal periods | 2 minutes 30 seconds |
| Billing retry period | 10 minutes |

## See Also

- [realTime](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime.md)
- [monthlyRenewalEveryHour](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryHour.md)
- [monthlyRenewalEveryThirtyMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtyMinutes.md)
- [monthlyRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFifteenMinutes.md)
- [monthlyRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds.md)

---


#### monthlyRenewalEveryHour

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case monthlyRenewalEveryHour
```

## 

The following table shows how this time rate affects subscriptions with various renewal periods in the testing environment:

| Subscription renewal period | Renewal time |
| --- | --- |
| Weekly | 15 minutes |
| Monthly | 1 hour |
| Bimonthly | 2 hours |
| Quarterly | 3 hours |
| Semiannually | 6 hours |
| Annually | 12 hours |

The sandbox environment also supports this subscription renewal rate. For more information about renewal rates in the sandbox environment, see [https://help.apple.com/app-store-connect/#/dev7e89e149d](https://help.apple.com/app-store-connect/#/dev7e89e149d).

The time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 12 minutes 51 seconds |
| Grace period for subscriptions with all other renewal periods | 30 minutes |
| Billing retry period | 2 hours |

## See Also

- [realTime](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime.md)
- [monthlyRenewalEveryThirtyMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtyMinutes.md)
- [monthlyRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFifteenMinutes.md)
- [monthlyRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFiveMinutes.md)
- [monthlyRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds.md)

---


#### monthlyRenewalEveryThirtyMinutes

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case monthlyRenewalEveryThirtyMinutes
```

## 

The following table shows how this time rate affects subscriptions with various renewal periods in the testing environment:

| Subscription renewal period | Renewal time |
| --- | --- |
| Weekly | 10 minutes |
| Monthly | 30 minutes |
| Bimonthly | 1 hour |
| Quarterly | 1 hour 30 minutes |
| Semiannually | 3 hours |
| Annually | 6 hours |

The sandbox environment also supports this subscription renewal rate. For more information about renewal rates in the sandbox environment, see [https://help.apple.com/app-store-connect/#/dev7e89e149d](https://help.apple.com/app-store-connect/#/dev7e89e149d).

The time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 8 minutes 34 seconds |
| Grace period for subscriptions with all other renewal periods | 15 minutes |
| Billing retry period | 1 hour |

## See Also

- [realTime](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime.md)
- [monthlyRenewalEveryHour](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryHour.md)
- [monthlyRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFifteenMinutes.md)
- [monthlyRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFiveMinutes.md)
- [monthlyRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds.md)

---


#### monthlyRenewalEveryThirtySeconds

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case monthlyRenewalEveryThirtySeconds
```

## 

The following table shows how this time rate affects subscriptions with various renewal periods in the testing environment:

| Subscription renewal period | Renewal time |
| --- | --- |
| Weekly | 10 seconds |
| Monthly | 30 seconds |
| Bimonthly | 1 minute |
| Quarterly | 1 minute 30 seconds |
| Semiannually | 3 minutes |
| Annually | 6 minutes |

The sandbox environment doesn’t have an equivalent subscription renewal rate for [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds). For more information about renewal rates in the sandbox environment, see [https://help.apple.com/app-store-connect/#/dev7e89e149d](https://help.apple.com/app-store-connect/#/dev7e89e149d).

The time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 9 seconds |
| Grace period for subscriptions with all other renewal periods | 15 seconds |
| Billing retry period | 1 minute |

## See Also

- [realTime](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime.md)
- [monthlyRenewalEveryHour](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryHour.md)
- [monthlyRenewalEveryThirtyMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtyMinutes.md)
- [monthlyRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFifteenMinutes.md)
- [monthlyRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFiveMinutes.md)

---


#### oneHourIsOneDay

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
case oneHourIsOneDay
```

## See Also

- [thirtyMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtyMinutesIsOneDay.md)
- [fiveMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/fiveMinutesIsOneDay.md)
- [oneMinuteIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneMinuteIsOneDay.md)
- [thirtySecondsIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtySecondsIsOneDay.md)
- [oneSecondIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneSecondIsOneDay.md)

---


#### oneMinuteIsOneDay

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
case oneMinuteIsOneDay
```

## See Also

- [oneHourIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneHourIsOneDay.md)
- [thirtyMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtyMinutesIsOneDay.md)
- [fiveMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/fiveMinutesIsOneDay.md)
- [thirtySecondsIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtySecondsIsOneDay.md)
- [oneSecondIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneSecondIsOneDay.md)

---


#### oneRenewalEveryFifteenMinutes

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case oneRenewalEveryFifteenMinutes
```

## 

This time rate renews subscriptions every fifteen minutes in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 15 minutes |
| Billing retry period | 30 minutes |

## See Also

- [oneRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes.md)
- [oneRenewalEveryMinute](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute.md)
- [oneRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds.md)
- [oneRenewalEveryTenSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds.md)
- [oneRenewalEveryTwoSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds.md)

---


#### oneRenewalEveryFiveMinutes

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case oneRenewalEveryFiveMinutes
```

## 

This time rate renews subscriptions every five minutes in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 5 minutes |
| Billing retry period | 10 minutes |

## See Also

- [oneRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes.md)
- [oneRenewalEveryMinute](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute.md)
- [oneRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds.md)
- [oneRenewalEveryTenSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds.md)
- [oneRenewalEveryTwoSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds.md)

---


#### oneRenewalEveryMinute

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case oneRenewalEveryMinute
```

## 

This time rate renews subscriptions every minute in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 1 minute |
| Billing retry period | 2 minutes |

## See Also

- [oneRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes.md)
- [oneRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes.md)
- [oneRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds.md)
- [oneRenewalEveryTenSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds.md)
- [oneRenewalEveryTwoSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds.md)

---


#### oneRenewalEveryTenSeconds

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case oneRenewalEveryTenSeconds
```

## 

This time rate renews subscriptions every ten seconds in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 10 seconds |
| Billing retry period | 20 seconds |

## See Also

- [oneRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes.md)
- [oneRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes.md)
- [oneRenewalEveryMinute](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute.md)
- [oneRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds.md)
- [oneRenewalEveryTwoSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds.md)

---


#### oneRenewalEveryThirtySeconds

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case oneRenewalEveryThirtySeconds
```

## 

This time rate renews subscriptions every thirty seconds in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 30 seconds |
| Billing retry period | 1 minute |

## See Also

- [oneRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes.md)
- [oneRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes.md)
- [oneRenewalEveryMinute](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute.md)
- [oneRenewalEveryTenSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds.md)
- [oneRenewalEveryTwoSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds.md)

---


#### oneRenewalEveryTwoSeconds

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case oneRenewalEveryTwoSeconds
```

## 

This time rate renews subscriptions every two seconds in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 2 seconds |
| Billing retry period | 4 seconds |

## See Also

- [oneRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes.md)
- [oneRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes.md)
- [oneRenewalEveryMinute](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute.md)
- [oneRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds.md)
- [oneRenewalEveryTenSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds.md)

---


#### oneSecondIsOneDay

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
case oneSecondIsOneDay
```

## See Also

- [oneHourIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneHourIsOneDay.md)
- [thirtyMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtyMinutesIsOneDay.md)
- [fiveMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/fiveMinutesIsOneDay.md)
- [oneMinuteIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneMinuteIsOneDay.md)
- [thirtySecondsIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtySecondsIsOneDay.md)

---


#### realTime

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case realTime
```

## 

With this time rate, subscriptions in the testing environment renew in real time. For example, a weekly subscription renews in one week.

The time rate also affects the billing grace period and the billing retry period in the testing environment. The table below shows the real-time rates:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 6 days |
| Grace period for subscriptions with all other renewal periods | 16 days |
| Billing retry period | 60 days |

## See Also

- [monthlyRenewalEveryHour](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryHour.md)
- [monthlyRenewalEveryThirtyMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtyMinutes.md)
- [monthlyRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFifteenMinutes.md)
- [monthlyRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFiveMinutes.md)
- [monthlyRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds.md)

---


#### thirtyMinutesIsOneDay

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
case thirtyMinutesIsOneDay
```

## See Also

- [oneHourIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneHourIsOneDay.md)
- [fiveMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/fiveMinutesIsOneDay.md)
- [oneMinuteIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneMinuteIsOneDay.md)
- [thirtySecondsIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtySecondsIsOneDay.md)
- [oneSecondIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneSecondIsOneDay.md)

---


#### thirtySecondsIsOneDay

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
case thirtySecondsIsOneDay
```

## See Also

- [oneHourIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneHourIsOneDay.md)
- [thirtyMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtyMinutesIsOneDay.md)
- [fiveMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/fiveMinutesIsOneDay.md)
- [oneMinuteIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneMinuteIsOneDay.md)
- [oneSecondIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneSecondIsOneDay.md)

---


### TimeRate-swift.enum

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum TimeRate
```

## 

The time rates that affect subscription renewals in the test environment match those in the sandbox environment with these exceptions:

- Only the test environment supports the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds) time rate.
- Only the test environment supports the fixed time rate options: [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes), [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes), [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute), [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds), [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds), and [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds).
- Only the sandbox environment supports a monthly renewal in 3 minutes.

For more information about time rates in the sandbox environment, see [https://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases](https://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases).

The time rates also affect the lengths of the billing retry period and the billing grace period in the testing environment. See the individual enumeration cases for the actual time values of the subscription renewal rates, billing retry periods, and billing grace periods.

## Topics

### Fixed time rates for subscription renewals

- [oneRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFifteenMinutes.md)
- [oneRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryFiveMinutes.md)
- [oneRenewalEveryMinute](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryMinute.md)
- [oneRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryThirtySeconds.md)
- [oneRenewalEveryTenSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTenSeconds.md)
- [oneRenewalEveryTwoSeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds.md)

### Scaled time rates for subscription renewals

- [realTime](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime.md)
- [monthlyRenewalEveryHour](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryHour.md)
- [monthlyRenewalEveryThirtyMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtyMinutes.md)
- [monthlyRenewalEveryFifteenMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFifteenMinutes.md)
- [monthlyRenewalEveryFiveMinutes](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryFiveMinutes.md)
- [monthlyRenewalEveryThirtySeconds](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/monthlyRenewalEveryThirtySeconds.md)

### Deprecated

- [oneHourIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneHourIsOneDay.md)
- [thirtyMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtyMinutesIsOneDay.md)
- [fiveMinutesIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/fiveMinutesIsOneDay.md)
- [oneMinuteIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneMinuteIsOneDay.md)
- [thirtySecondsIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/thirtySecondsIsOneDay.md)
- [oneSecondIsOneDay](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneSecondIsOneDay.md)

### Initializers

- [init(rawValue:)](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum/init(rawValue:).md)

## See Also

- [timeRate-swift.property](../com.apple.storekittest/StoreKitTest/SKTestSession/timeRate-swift.property.md)
- [enableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:).md)
- [disableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:).md)
- [forceRenewalOfSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:).md)
- [expireSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:).md)

---


### allTransactions()

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func allTransactions() -> [SKTestTransaction]
```

## 

An array that contains all transactions.

## 

This array contains all transactions, including those that don’t appear in the receipt, such as:

- Failed transactions
- Pending Ask to Buy transactions
- Purchases of consumable products

Use this list to work with Ask to Buy, to refund a specific transaction, or delete a transaction from the history, so you can repeat the test.

## See Also

- [deleteTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/deleteTransaction(identifier:).md)
- [clearTransactions()](../com.apple.storekittest/StoreKitTest/SKTestSession/clearTransactions().md)

---


### approveAskToBuyTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func approveAskToBuyTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of the Ask to Buy transaction.

## See Also

- [askToBuyEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/askToBuyEnabled.md)
- [declineAskToBuyTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:).md)

---


### askToBuyEnabled

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var askToBuyEnabled: Bool { get set }
```

## 

The default value is `false`. Enabling this property causes all purchases to require approval until you disable it. To approve the purchase in the testing environment, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:)), and to decline it, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:)).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [approveAskToBuyTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:).md)
- [declineAskToBuyTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:).md)

---


### billingGracePeriodIsEnabled

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var billingGracePeriodIsEnabled: Bool { get set }
```

## 

The default value is `false`. The value of this property has no effect when [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal) is `false`.

In the production environment, you indicate whether your app supports a billing grace period by setting it in App Store Connect. In the testing environment, you indicate that your app supports it by setting the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled) property to `true`.

To test how your app handles a grace period when a subscription enters a billing retry state, enable [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal) and [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled). All subscriptions fail to renew with a simulated billing issue until you set [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal) to `false`. To resolve a billing issue in the testing environment, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)).

For more information about billing grace periods and enabling them in the production environment, see [doc://com.apple.documentation/documentation/StoreKit/reducing-involuntary-subscriber-churn](doc://com.apple.documentation/documentation/StoreKit/reducing-involuntary-subscriber-churn) and [https://help.apple.com/app-store-connect/#/dev58bda3212](https://help.apple.com/app-store-connect/#/dev58bda3212).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [shouldEnterBillingRetryOnRenewal](../com.apple.storekittest/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal.md)
- [resolveIssueForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:).md)

---


### buyProduct(identifier:options:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
@discardableResult func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption> = []) async throws -> Transaction
```

## See Also

- [setSimulatedError(_:forAPI:)](../com.apple.storekittest/StoreKitTest/SKTestSession/setSimulatedError(_:forAPI:).md)
- [simulatedError(forAPI:)](../com.apple.storekittest/StoreKitTest/SKTestSession/simulatedError(forAPI:).md)

---


### buyProduct(productIdentifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
func buyProduct(productIdentifier: String) throws
```

## Parameters

- **productIdentifier**: Product identifier of the in-app purchase.

## 

After calling this function, handle the new transaction in your payment queue.

## See Also

- [refundTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/refundTransaction(identifier:).md)

---


### clearTransactions()

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func clearTransactions()
```

## 

After you clear the transactions from the test environment, the test environment produces an empty receipt. Use this method to enable repeating tests for one-time purchases.

To revert all the settings in the test environment to those in the StoreKit configuration file, see [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()).

## See Also

- [allTransactions()](../com.apple.storekittest/StoreKitTest/SKTestSession/allTransactions().md)
- [deleteTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/deleteTransaction(identifier:).md)

---


### consentToPriceIncreaseForTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func consentToPriceIncreaseForTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of the auto-renewable subscription that has a pending price increase.

## 

To test how your app handles the price increase consent flow for auto-renewable subscriptions, first call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)).

Call the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:)) method to simulate a user consenting to the price increase. This method removes the subscription’s pending price increase status. The subscription renews at the next billing period.

## See Also

- [requestPriceIncreaseConsentForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:).md)
- [declinePriceIncreaseForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:).md)

---


### declineAskToBuyTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func declineAskToBuyTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of an Ask to Buy transaction.

## See Also

- [askToBuyEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/askToBuyEnabled.md)
- [approveAskToBuyTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:).md)

---


### declinePriceIncreaseForTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func declinePriceIncreaseForTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of the auto-renewable subscription that has a pending price increase.

## 

To test how your app handles the price increase consent flow for auto-renewable subscriptions, first call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)).

Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:)) to simulate a user canceling the subscription. Specifically, this method disables auto-renew and removes the subscription’s pending price increase status. The subscription expires at the end of the billing period in the testing environment.

## See Also

- [requestPriceIncreaseConsentForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:).md)
- [consentToPriceIncreaseForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:).md)

---


### deleteTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func deleteTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction identifier.

## 

When you delete a transaction, the test environment also removes the existing transaction from the receipt. Some transactions don’t appear in the receipt, including finished consumable purchases, failed purchases, Ask To Buy transactions pending approval, and restored purchases. Deleting a transaction deletes its child transactions, for example:

- Deleting an original subscription transaction deletes all related renewal transactions.
- Deleting a transaction deletes any associated restored transactions.

## See Also

- [allTransactions()](../com.apple.storekittest/StoreKitTest/SKTestSession/allTransactions().md)
- [clearTransactions()](../com.apple.storekittest/StoreKitTest/SKTestSession/clearTransactions().md)

---


### disableAutoRenewForTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func disableAutoRenewForTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of the auto-renewable subscription.

## 

Call this method to disable auto-renewing for a subscription. A subscription with auto-renew disabled expires at the end of the billing period and doesn’t renew at the start of the next billing period.

## See Also

- [timeRate-swift.property](../com.apple.storekittest/StoreKitTest/SKTestSession/timeRate-swift.property.md)
- [TimeRate-swift.enum](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum.md)
- [enableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:).md)
- [forceRenewalOfSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:).md)
- [expireSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:).md)

---


### disableDialogs

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var disableDialogs: Bool { get set }
```

## 

The default value is `false`. Set this value to `true` when you run automated tests and want to suppress interactive dialogs.

## See Also

- [storefront](../com.apple.storekittest/StoreKitTest/SKTestSession/storefront.md)
- [locale](../com.apple.storekittest/StoreKitTest/SKTestSession/locale.md)

---


### enableAutoRenewForTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func enableAutoRenewForTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of the auto-renewable subscription.

## 

Call this method to enable the subscription to automatically renew in the testing environment. By default, all auto-renewable subscriptions have auto-renew enabled.

## See Also

- [timeRate-swift.property](../com.apple.storekittest/StoreKitTest/SKTestSession/timeRate-swift.property.md)
- [TimeRate-swift.enum](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum.md)
- [disableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:).md)
- [forceRenewalOfSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:).md)
- [expireSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:).md)

---


### expireSubscription(productIdentifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func expireSubscription(productIdentifier: String) throws
```

## Parameters

- **productIdentifier**: The [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/productIdentifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/productIdentifier) of the auto-renewable subscription to expire.

## 

Use this method to test how your app handles expired subscriptions and revoking access to content or service. This method forces the subscription to expire. Specifically, the testing environment disables auto-renew and changes the subscription’s expiration date to the current system time.

You can also test subscription expiration by accelerating the time in the testing environment to speed up subscription renewal periods. See [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property) for more information.

## See Also

- [timeRate-swift.property](../com.apple.storekittest/StoreKitTest/SKTestSession/timeRate-swift.property.md)
- [TimeRate-swift.enum](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum.md)
- [enableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:).md)
- [disableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:).md)
- [forceRenewalOfSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:).md)

---


### failTransactionsEnabled

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
var failTransactionsEnabled: Bool { get set }
```

## 

The default value is `false`. Set this value to `true` when you want to test your app’s response to [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction) transactions that fail. Attempted transactions in the payment queue show the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransactionState/failed](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransactionState/failed) state, with the error code that you set in [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/failureError](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/failureError).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [failureError](../com.apple.storekittest/StoreKitTest/SKTestSession/failureError.md)

---


### failureError

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS

```swift
var failureError: SKError.Code { get set }
```

## 

You can force an error by setting [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/failTransactionsEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/failTransactionsEnabled) to `true` and setting [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/failureError](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/failureError) value to one of these supported error codes: [doc://com.apple.documentation/documentation/StoreKit/SKError/Code/unknown](doc://com.apple.documentation/documentation/StoreKit/SKError/Code/unknown), [doc://com.apple.documentation/documentation/StoreKit/SKError/Code/invalidOfferIdentifier](doc://com.apple.documentation/documentation/StoreKit/SKError/Code/invalidOfferIdentifier), [doc://com.apple.documentation/documentation/StoreKit/SKError/Code/invalidSignature](doc://com.apple.documentation/documentation/StoreKit/SKError/Code/invalidSignature), [doc://com.apple.documentation/documentation/StoreKit/SKError/Code/missingOfferParams](doc://com.apple.documentation/documentation/StoreKit/SKError/Code/missingOfferParams), [doc://com.apple.documentation/documentation/StoreKit/SKError/Code/invalidOfferPrice](doc://com.apple.documentation/documentation/StoreKit/SKError/Code/invalidOfferPrice).

Use these settings to test your how your app responds to failed transactions.

## See Also

- [failTransactionsEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/failTransactionsEnabled.md)

---


### forceRenewalOfSubscription(productIdentifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func forceRenewalOfSubscription(productIdentifier: String) throws
```

## Parameters

- **productIdentifier**: The [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/productIdentifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/productIdentifier) of the auto-renewable subscription to renew.

## 

Use this method to test how your code handles subscription renewals. When you call this method, the subscription expires at the time you call the method, and a new subscription period begins.

To force the subscription renewal, the testing environment changes the [doc://com.apple.documentation/documentation/StoreKit/Transaction/expirationDate](doc://com.apple.documentation/documentation/StoreKit/Transaction/expirationDate) property on the [doc://com.apple.documentation/documentation/StoreKit/Transaction](doc://com.apple.documentation/documentation/StoreKit/Transaction) to the current system time. (If your app uses receipts, the receipt also shows this expiration date change). The testing environment also:

- Enables the subscription auto-renew state
- Removes a pending price increase, setting it to [doc://com.apple.documentation/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/PriceIncreaseStatus-swift.enum/noIncreasePending](doc://com.apple.documentation/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/PriceIncreaseStatus-swift.enum/noIncreasePending)

The testing environment doesn’t change the billing retry state with this call.

You can also test subscription renewals by accelerating the time in the testing environment to speed up subscription renewal periods. See [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property) for more information.

## See Also

- [timeRate-swift.property](../com.apple.storekittest/StoreKitTest/SKTestSession/timeRate-swift.property.md)
- [TimeRate-swift.enum](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum.md)
- [enableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:).md)
- [disableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:).md)
- [expireSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:).md)

---


### init(configurationFileNamed:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
convenience init(configurationFileNamed filename: String) throws
```

## Parameters

- **filename**: A StoreKit configuration file that you include in your application’s bundle.

## 

Create a configuration file in Xcode by selecting File > New > File and choosing StoreKit Configuration File. By default, the filename is `Configuration.storekit`. You can include multiple configuration files in your project, but only one can be active at a time. StoreKit configuration files always have a .`storekit` file extension.

To return all settings in the test session to the states defined in this configuration file, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()).

## See Also

- [init(contentsOf:)](../com.apple.storekittest/StoreKitTest/SKTestSession/init(contentsOf:).md)
- [resetToDefaultState()](../com.apple.storekittest/StoreKitTest/SKTestSession/resetToDefaultState().md)

---


### init(contentsOf:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
init(contentsOf fileURL: URL) throws
```

## Parameters

- **fileURL**: A file URL for a configuration file with a .`storekit` extension.

## 

The file must have a `.storekit` extension. Create a configuration file in Xcode by selecting File > New > File and choosing StoreKit Configuration File.

To return all settings in the test session to the states defined in this StoreKit configuration file, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()).

## See Also

- [init(configurationFileNamed:)](../com.apple.storekittest/StoreKitTest/SKTestSession/init(configurationFileNamed:).md)
- [resetToDefaultState()](../com.apple.storekittest/StoreKitTest/SKTestSession/resetToDefaultState().md)

---


### interruptedPurchasesEnabled

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var interruptedPurchasesEnabled: Bool { get set }
```

## 

The default value is `false`. Enabling this property causes all purchases to fail until you disable it.

During testing, resolve the interrupted purchase by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)) for the affected transaction.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [resolveIssueForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:).md)

---


### locale

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var locale: Locale { get set }
```

## 

This value determines the locale the test environment uses when it fetches localized metadata for [doc://com.apple.documentation/documentation/StoreKit/SKProductsRequest](doc://com.apple.documentation/documentation/StoreKit/SKProductsRequest). You provide localized metadata in your StoreKit configuration file.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [storefront](../com.apple.storekittest/StoreKitTest/SKTestSession/storefront.md)
- [disableDialogs](../com.apple.storekittest/StoreKitTest/SKTestSession/disableDialogs.md)

---


### refundTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func refundTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of an in-app purchase to get a refund.

## 

In the testing environment, the system always approves refund requests, and processes them immediately. You can choose the reason for the refund by using [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj) in your app and selecting a reason. (Your app may also use [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph), [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd), or [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd).  If your app uses SwiftUI, it may use [doc://com.apple.documentation/documentation/SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:)](doc://com.apple.documentation/documentation/SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:)).) Otherwise, the refund reason defaults to [doc://com.apple.documentation/documentation/StoreKit/Transaction/RevocationReason-swift.struct/other](doc://com.apple.documentation/documentation/StoreKit/Transaction/RevocationReason-swift.struct/other).

After calling this function, handle the new transaction in [doc://com.apple.documentation/documentation/StoreKit/Transaction/updates](doc://com.apple.documentation/documentation/StoreKit/Transaction/updates) or in your payment queue. Look for the [doc://com.apple.documentation/documentation/StoreKit/Transaction/revocationDate](doc://com.apple.documentation/documentation/StoreKit/Transaction/revocationDate) and [doc://com.apple.documentation/documentation/StoreKit/Transaction/revocationReason-swift.property](doc://com.apple.documentation/documentation/StoreKit/Transaction/revocationReason-swift.property) properties, which indicate the refund.

## See Also

- [buyProduct(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/buyProduct(productIdentifier:).md)

---


### requestPriceIncreaseConsentForTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func requestPriceIncreaseConsentForTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) of the auto-renewable subscription to get a pending price increase.

## 

Use this method to test how your app handles a price increase consent flow. When you call this method, the testing environment assigns a pending price increase to the subscription indicated by the `identifier`. It also sends the price increase consent message to your app. Note that in the testing environment, changing the price of the subscription is optional.

You may call this method repeatedly to prompt the testing environment to send the price increase consent message.

> **NOTE:** The system displays a price increase consent sheet in iOS only. On other supported platforms, use [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)) to test that your app handles the subscription status update correctly.

By default, if your app doesn’t listen for [doc://com.apple.documentation/documentation/StoreKit/Message/messages-swift.type.property](doc://com.apple.documentation/documentation/StoreKit/Message/messages-swift.type.property) or implement [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)), the system displays the price increase consent sheet immediately. Your app may delay displaying the sheet to ensure a good user experience. For more information, see [doc://com.apple.documentation/documentation/StoreKit/Message/Messages-swift.struct](doc://com.apple.documentation/documentation/StoreKit/Message/Messages-swift.struct) for apps that run in iOS 16 and later, and [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)) and [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/showPriceConsentIfNeeded()](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/showPriceConsentIfNeeded()) for apps that run in earlier versions.

When the system displays the price increase consent sheet, it awaits a response from the user, which may be one of the following:

- The user consents to the price increase.
- The user does nothing. The subscription expires at the end of the subscription period.
- The user cancels the subscription.

See the sections below for information about simulating these user responses in the testing environment. The system removes the pending price increase status when the user consents to the price increase, the subscription expires, or the user cancels the subscription and auto-renew is disabled.

For more information about increasing prices of auto-renewable subscriptions, see [https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers](https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers).

### 

Start with [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs) set to `false`, so the system displays the price increase consent sheet in the testing environment.

To simulate a user consenting to a price increase, the tester consents to the price increase in the sheet. The auto-renewable subscription renews at the next renewal period.

To simulate a user not responding to the price increase, the tester closes the price increase consent sheet without consenting. The auto-renewable subscription expires at the end of the renewal period because the user didn’t consent to the price increase. To speed up the subscription expiration in the testing environment, set a shorter time rate in the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property) variable.

To simulate a user canceling their subscription, the tester closes the price increase consent sheet without consenting. On the next sheet, select to cancel the subscription. The auto-renewable subscription doesn’t renew at the next renewal period.

### 

Start with [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs) set to `true`, so the system doesn’t displays the price increase consent sheet in the testing environment.

> **NOTE:** The system doesn’t display any sheets in the testing environment if [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs) is `true`.

To simulate a user consenting to a price increase, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:)). The auto-renewable subscription renews at the next renewal period.

To simulate a user not responding to the price increase consent, wait until the end of the subscription’s renewal period. The auto-renewable subscription expires because the user didn’t consent to the price increase. To speed up the subscription expiration in the testing environment, set a shorter time rate in the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property) variable.

To simulate the user canceling their subscription, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:)). The subscription doesn’t renew at the next renewal period because the auto-renew setting is off.

## See Also

- [consentToPriceIncreaseForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:).md)
- [declinePriceIncreaseForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:).md)

---


### resetToDefaultState()

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func resetToDefaultState()
```

## 

During testing, your tests may override the property settings such as the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property), [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/askToBuyEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/askToBuyEnabled), [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/interruptedPurchasesEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/interruptedPurchasesEnabled), and [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled). Call this method to revert all the property settings to the states defined in the StoreKit configuration file that you use to initialize this [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession) instance.

See [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/clearTransactions()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/clearTransactions()) to remove all transactions from the testing environment.

## See Also

- [init(configurationFileNamed:)](../com.apple.storekittest/StoreKitTest/SKTestSession/init(configurationFileNamed:).md)
- [init(contentsOf:)](../com.apple.storekittest/StoreKitTest/SKTestSession/init(contentsOf:).md)

---


### resolveIssueForTransaction(identifier:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func resolveIssueForTransaction(identifier: Int) throws
```

## Parameters

- **identifier**: The transaction [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) for the transaction that the test environment resolves.

## 

Call this method to simulate a user resolving an issue that prevents a purchase, such as an interrupted purchase or a billing issue. You enable the testing environment to simulate the issues by setting the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/interruptedPurchasesEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/interruptedPurchasesEnabled) and [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled) properties, respectively.

In the production environment, users resolve the issues by completing actions outside of your app. For example, users may need to agree to new terms and conditions or update a payment card.

When you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)), your app receives the new transaction in the [doc://com.apple.documentation/documentation/StoreKit/Transaction/updates](doc://com.apple.documentation/documentation/StoreKit/Transaction/updates) sequence or the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/transactionObservers](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/transactionObservers).

## See Also

- [interruptedPurchasesEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/interruptedPurchasesEnabled.md)

---


### setSimulatedError(_:forAPI:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func setSimulatedError<API>(_ error: API.Failure?, forAPI api: API) async throws where API : FailableStoreKitAPI
```

## See Also

- [buyProduct(identifier:options:)](../com.apple.storekittest/StoreKitTest/SKTestSession/buyProduct(identifier:options:).md)
- [simulatedError(forAPI:)](../com.apple.storekittest/StoreKitTest/SKTestSession/simulatedError(forAPI:).md)

---


### shouldEnterBillingRetryOnRenewal

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var shouldEnterBillingRetryOnRenewal: Bool { get set }
```

## 

The default value is `false`.

While this property is enabled, all renewals of auto-renewable subscriptions in the test environment fail due to a simulated billing issue and enter a billing retry state. To resolve the simulated billing issue, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)) for the affected auto-renewable subscription.

The [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property) value determines the length of the billing retry period in the testing environment.

## See Also

- [billingGracePeriodIsEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled.md)
- [resolveIssueForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:).md)

---


### simulatedError(forAPI:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
func simulatedError<API>(forAPI api: API) async -> API.Failure? where API : FailableStoreKitAPI
```

## See Also

- [buyProduct(identifier:options:)](../com.apple.storekittest/StoreKitTest/SKTestSession/buyProduct(identifier:options:).md)
- [setSimulatedError(_:forAPI:)](../com.apple.storekittest/StoreKitTest/SKTestSession/setSimulatedError(_:forAPI:).md)

---


### storefront

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var storefront: String { get set }
```

## 

This property uses the ISO 3166-1 alpha-3 region code representation. The default value is `USA`.

In the testing environment, this variable determines the value of the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/storefront](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/storefront) variable on your app’s payment queue, and affects the currency type displayed in the payment sheet.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [locale](../com.apple.storekittest/StoreKitTest/SKTestSession/locale.md)
- [disableDialogs](../com.apple.storekittest/StoreKitTest/SKTestSession/disableDialogs.md)

---


### timeRate-swift.property

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var timeRate: SKTestSession.TimeRate { get set }
```

## 

Use the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/timeRate-swift.property) value when you test auto-renewable subscriptions to speed up or slow down the time it takes for subscriptions to renew in the test environment. The default value is [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/realTime). For maximum accelerated time, use [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum/oneRenewalEveryTwoSeconds).

To test subscription renewals, you can also call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:)) to prompt a subscription to renew immediately.

The time rate also affects the length of the billing retry period and the billing grace period in the test environment. See the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/TimeRate-swift.enum) enumeration for the actual time values of each case.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resetToDefaultState()) to revert all settings to those in the configuration file.

## See Also

- [TimeRate-swift.enum](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum.md)
- [enableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:).md)
- [disableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:).md)
- [forceRenewalOfSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:).md)
- [expireSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:).md)

---


## SKTestTransaction


### autoRenewingEnabled

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var autoRenewingEnabled: Bool { get }
```

## 

By default, the system creates subscriptions with auto-renew enabled. To disable auto-renew, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:)).

## See Also

- [hasPurchaseIssue](../com.apple.storekittest/StoreKitTest/SKTestTransaction/hasPurchaseIssue.md)
- [isPendingPriceIncreaseConsent](../com.apple.storekittest/StoreKitTest/SKTestTransaction/isPendingPriceIncreaseConsent.md)
- [pendingAskToBuyConfirmation](../com.apple.storekittest/StoreKitTest/SKTestTransaction/pendingAskToBuyConfirmation.md)

---


### cancelDate

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var cancelDate: Date? { get }
```

## 

The [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate) is equivalent to the [doc://com.apple.documentation/documentation/StoreKit/Transaction/revocationDate](doc://com.apple.documentation/documentation/StoreKit/Transaction/revocationDate) in [doc://com.apple.documentation/documentation/StoreKit/Transaction](doc://com.apple.documentation/documentation/StoreKit/Transaction). The system sets the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate) if it refunds or revokes the in-app purchase. Otherwise, the value is `nil`.

A subscription can have a `nil` [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate) and be inactive if its expiration date passed.

The system doesn’t set [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate) if the user turns off auto-renewing for the subscription. If the user upgrades the subscription, the system sets [doc://com.apple.documentation/documentation/StoreKit/Transaction/isUpgraded](doc://com.apple.documentation/documentation/StoreKit/Transaction/isUpgraded) in [doc://com.apple.documentation/documentation/StoreKit/Transaction](doc://com.apple.documentation/documentation/StoreKit/Transaction) to `true` and sends a new transaction for the upgraded subscription. The system doesn’t set [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/cancelDate) in this case.

## See Also

- [purchaseDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/purchaseDate.md)
- [expirationDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/expirationDate.md)

---


### expirationDate

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var expirationDate: Date? { get }
```

## 

The test environment sets the expiration date based on the subscription settings in your active StoreKit configuration file.

## See Also

- [purchaseDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/purchaseDate.md)
- [cancelDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/cancelDate.md)

---


### hasPurchaseIssue

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var hasPurchaseIssue: Bool { get }
```

## 

To test interrupted purchases, first set [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/interruptedPurchasesEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/interruptedPurchasesEnabled) to `true` before making a purchase. If [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/hasPurchaseIssue](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/hasPurchaseIssue) value is `true`, then resolve the identified transaction by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)).

## See Also

- [autoRenewingEnabled](../com.apple.storekittest/StoreKitTest/SKTestTransaction/autoRenewingEnabled.md)
- [isPendingPriceIncreaseConsent](../com.apple.storekittest/StoreKitTest/SKTestTransaction/isPendingPriceIncreaseConsent.md)
- [pendingAskToBuyConfirmation](../com.apple.storekittest/StoreKitTest/SKTestTransaction/pendingAskToBuyConfirmation.md)

---


### identifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var identifier: Int { get }
```

## 

To get a list of all the transactions available in the testing environment, see [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/allTransactions()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/allTransactions()).

Use this [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/identifier) if you want to perform actions on the transaction in the testing environment, such as:

- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/deleteTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/deleteTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/refundTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/refundTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:))

## See Also

- [originalTransactionIdentifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/originalTransactionIdentifier.md)
- [productIdentifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/productIdentifier.md)

---


### isPendingPriceIncreaseConsent

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var isPendingPriceIncreaseConsent: Bool { get }
```

## 

This value applies only to subscription price increases that require customer consent in the test environment.

## See Also

- [autoRenewingEnabled](../com.apple.storekittest/StoreKitTest/SKTestTransaction/autoRenewingEnabled.md)
- [hasPurchaseIssue](../com.apple.storekittest/StoreKitTest/SKTestTransaction/hasPurchaseIssue.md)
- [pendingAskToBuyConfirmation](../com.apple.storekittest/StoreKitTest/SKTestTransaction/pendingAskToBuyConfirmation.md)

---


### originalTransactionIdentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var originalTransactionIdentifier: Int { get }
```

## 

For subscription renewals, or if you restore a purchase, the [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/originalTransactionIdentifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/originalTransactionIdentifier) is the original transaction for that subscription or in-app purchase.

## See Also

- [identifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/identifier.md)
- [productIdentifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/productIdentifier.md)

---


### pendingAskToBuyConfirmation

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var pendingAskToBuyConfirmation: Bool { get }
```

## 

To test an Ask to Buy scenario, first set [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/askToBuyEnabled](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/askToBuyEnabled) to `true` before making a purchase. If [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/pendingAskToBuyConfirmation](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction/pendingAskToBuyConfirmation) is `true`, approve the transaction by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:)) , or decline it by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:)).

## See Also

- [autoRenewingEnabled](../com.apple.storekittest/StoreKitTest/SKTestTransaction/autoRenewingEnabled.md)
- [hasPurchaseIssue](../com.apple.storekittest/StoreKitTest/SKTestTransaction/hasPurchaseIssue.md)
- [isPendingPriceIncreaseConsent](../com.apple.storekittest/StoreKitTest/SKTestTransaction/isPendingPriceIncreaseConsent.md)

---


### productIdentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var productIdentifier: String { get }
```

## 

You configure the product identifiers in the .`storekit` configuration file. Each product identifier must be unique.

> **NOTE:** The StoreKitTest framework never accesses App Store Connect, so it doesn’t retrieve actual product identifiers you may have configured there.

## See Also

- [identifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/identifier.md)
- [originalTransactionIdentifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/originalTransactionIdentifier.md)

---


### purchaseDate

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var purchaseDate: Date { get }
```

## 

The purchase date applies to any type of in-app purchase.

## See Also

- [cancelDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/cancelDate.md)
- [expirationDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/expirationDate.md)

---


### state

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
var state: SKPaymentTransactionState { get }
```

## 

The transaction states in the test environment are the same states that StoreKit uses in production.

---


## failablestorekitapi


### failure

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
associatedtype Failure : SKTestFailure
```

---


## skadtesterror


### conflictingsource

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var conflictingSource: SKAdTestError.Code { get }
```

## See Also

- [invalidCampaignId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidCampaignId.md)
- [signatureMissingCampaignId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingCampaignId.md)

---


### excessivepostbacks

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var excessivePostbacks: SKAdTestError.Code { get }
```

## 

The maximum number of postbacks allowed in the `postbacks` array in [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) is six.

## See Also

- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### invalidcampaignid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidCampaignId: SKAdTestError.Code { get }
```

## 

A campaign ID is an integer that is greater than or equal to one and less than or equal to one hundred.

## See Also

- [signatureMissingCampaignId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingCampaignId.md)
- [conflictingSource](../com.apple.storekittest/StoreKitTest/SKAdTestError/conflictingSource.md)

---


### invalidconversionvalue

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidConversionValue: SKAdTestError.Code { get }
```

## 

This error isn’t used. If your conversion value isn’t valid, the unit test shows the [doc://com.apple.documentation/documentation/StoreKit/SKANError-swift.struct/Code/invalidConversionValue](doc://com.apple.documentation/documentation/StoreKit/SKANError-swift.struct/Code/invalidConversionValue) error instead, but only if your app calls [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)).

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### invalidimpressionid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidImpressionId: SKAdTestError.Code { get }
```

## See Also

- [invalidVersion](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidVersion.md)
- [invalidSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceAppAdamId.md)
- [invalidSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceDomain.md)
- [invalidSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceIdentifier.md)
- [unknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/unknownError.md)

---


### invalidpostbackurl

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidPostbackURL: SKAdTestError.Code { get }
```

## 

Check that the URL is valid in the [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/postbackURL](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/postbackURL) parameter in [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback).

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### invalidrunneruppostback

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidRunnerUpPostback: SKAdTestError.Code { get }
```

## 

Check that all non-winning postback you create with [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)) in [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback) specify version 3 ([doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion/version3_0](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion/version3_0)) or later. Non-winning postbacks are available starting in version 3. For more information about versions, see [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### invalidsourceappadamid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidSourceAppAdamId: SKAdTestError.Code { get }
```

## See Also

- [invalidVersion](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidVersion.md)
- [invalidImpressionId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidImpressionId.md)
- [invalidSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceDomain.md)
- [invalidSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceIdentifier.md)
- [unknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/unknownError.md)

---


### invalidsourcedomain

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidSourceDomain: SKAdTestError.Code { get }
```

## 

For more information about formatting source domains, see the `source_domain` property of [doc://com.apple.documentation/documentation/SKAdNetworkforWebAds/AdImpressionResponse](doc://com.apple.documentation/documentation/SKAdNetworkforWebAds/AdImpressionResponse).

## See Also

- [invalidVersion](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidVersion.md)
- [invalidImpressionId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidImpressionId.md)
- [invalidSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceAppAdamId.md)
- [invalidSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceIdentifier.md)
- [unknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/unknownError.md)

---


### invalidsourceidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidSourceIdentifier: SKAdTestError.Code { get }
```

## 

A valid postback includes two to four digits of the impression’s [doc://com.apple.documentation/documentation/StoreKit/SKAdImpression/sourceIdentifier](doc://com.apple.documentation/documentation/StoreKit/SKAdImpression/sourceIdentifier). For more information about the varying length of source identifiers, see [doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows](doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [invalidVersion](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidVersion.md)
- [invalidImpressionId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidImpressionId.md)
- [invalidSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceAppAdamId.md)
- [invalidSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceDomain.md)
- [unknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/unknownError.md)

---


### invalidversion

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidVersion: SKAdTestError.Code { get }
```

## See Also

- [invalidImpressionId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidImpressionId.md)
- [invalidSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceAppAdamId.md)
- [invalidSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceDomain.md)
- [invalidSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceIdentifier.md)
- [unknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/unknownError.md)

---


### invalidwinningpostbackcount

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var invalidWinningPostbackCount: SKAdTestError.Code { get }
```

## 

A valid session has one or three winning postbacks.

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### malformedpostbacks

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var malformedPostbacks: SKAdTestError.Code { get }
```

## 

Check that all parameters in the postback use the correct type.

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### misplacedwinnerpostback

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var misplacedWinnerPostback: SKAdTestError.Code { get }
```

## 

Check that the first postback in the `postbacks` array you provide to [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) is marked as a winning postback, with `didWin` set to `true`. Check that the winning postback is in no other position in the array.

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### missingpostbacks

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var missingPostbacks: SKAdTestError.Code { get }
```

## 

Check that the `postbacks` array you provide when calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) isn’t empty.

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### missingsignature

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var missingSignature: SKAdTestError.Code { get }
```

## 

Check that you provide a signature in [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)) or [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)).

## See Also

- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### missingwinningpostback

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var missingWinningPostback: SKAdTestError.Code { get }
```

## 

Check that the first postback in the `postbacks` array you set when calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) has `didWin` set to `true`.

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### nopendingpostbacks

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var noPendingPostbacks: SKAdTestError.Code { get }
```

## 

This error occurs if you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)) before adding a postback to the test session ([doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession)). To avoid this error, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback) to create a test postback, and [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) to add the test postback to the test session before calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)).

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

---


### signatureinvalidkey

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureInvalidKey: SKAdTestError.Code { get }
```

## 

The public key that you provide in the [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)) or [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)) methods must be a key that uses Elliptic Curve Digital Signature Algorithm (ECDSA) with a prime256v1 curve. For more information about the key, see [doc://com.apple.documentation/documentation/StoreKit/registering-an-ad-network](doc://com.apple.documentation/documentation/StoreKit/registering-an-ad-network).

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signatureinvalidorder

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureInvalidOrder: SKAdTestError.Code { get }
```

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingadnetworkid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingAdNetworkId: SKAdTestError.Code { get }
```

## 

Be sure to include an ad network identifier when you create and validate an ad impression in the testing environment.

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingappadamid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingAppAdamId: SKAdTestError.Code { get }
```

## 

Be sure to include the app item identifier for the advertised app when you create and validate an ad impression in the testing environment.

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingcampaignid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingCampaignId: SKAdTestError.Code { get }
```

## 

Be sure to include the campaign identifier when you create and validate an ad impression in the testing environment.

## See Also

- [invalidCampaignId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidCampaignId.md)
- [conflictingSource](../com.apple.storekittest/StoreKitTest/SKAdTestError/conflictingSource.md)

---


### signaturemissingfidelitytype

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingFidelityType: SKAdTestError.Code { get }
```

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingnonce

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingNonce: SKAdTestError.Code { get }
```

## 

Be sure to include a nonce when you create and validate an ad impression in the testing environment.

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingsourceappadamid

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingSourceAppAdamId: SKAdTestError.Code { get }
```

## 

Be sure to include the app item identifier for the source app when you create and validate an ad impression in the testing environment.

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingsourcedomain

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingSourceDomain: SKAdTestError.Code { get }
```

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingsourceidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingSourceIdentifier: SKAdTestError.Code { get }
```

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signaturemissingtimestamp

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureMissingTimestamp: SKAdTestError.Code { get }
```

## 

Be sure to include a timestamp when you create and validate an ad impression in the testing environment.

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signatureunknownerror

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureUnknownError: SKAdTestError.Code { get }
```

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

---


### signatureverificationfailed

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var signatureVerificationFailed: SKAdTestError.Code { get }
```

## 

The ad impression signature isn’t valid. Check the following:

- You use the same cryptographic key-pair when you sign the ad impression and validate it in the testing environment. If you use different key pairs in these two steps, signature verification will fail. For more information about signing the ad, see [doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads](doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads). For more information about validating the ad impression in the testing environment, see [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)) and [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)).
- You use the correct signature instructions for the SKAdNetwork version that your app uses. For more information about SKAdNetwork versions, see [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).
- Your signature contains all the parameters in the correct order for the version you’re using.
- Your signature uses the correct separator character.

For more information about signatures, see [doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads](doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads).

## See Also

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)

---


### unknownerror

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var unknownError: SKAdTestError.Code { get }
```

## See Also

- [invalidVersion](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidVersion.md)
- [invalidImpressionId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidImpressionId.md)
- [invalidSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceAppAdamId.md)
- [invalidSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceDomain.md)
- [invalidSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceIdentifier.md)

---


### unlinkedwinningpostbacks

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static var unlinkedWinningPostbacks: SKAdTestError.Code { get }
```

## 

To create linked winning postbacks for testing multiple conversion windows, use the [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:)) method.

## See Also

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)

---


## skadtestpostback


### adcampaignidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var adCampaignIdentifier: Int { get }
```

## 

Ad networks set their own campaign identifiers, which must be an integer between 1 and 100.

## See Also

- [conversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/conversionValue.md)

---


### adnetworkidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var adNetworkIdentifier: String { get }
```

## 

Check that the ad network identifier string is lowercased.

## See Also

- [appStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/appStoreItemIdentifier.md)
- [sourceAppStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier.md)
- [sourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceDomain.md)
- [sourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceIdentifier.md)

---


### appstoreitemidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var appStoreItemIdentifier: Int { get }
```

## See Also

- [adNetworkIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adNetworkIdentifier.md)
- [sourceAppStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier.md)
- [sourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceDomain.md)
- [sourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceIdentifier.md)

---


### coarseconversionvalue

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var coarseConversionValue: SKAdNetwork.CoarseConversionValue? { get }
```

## 

A postback in SKAdNetwork version 4 and later provides a [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fineConversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fineConversionValue) or this [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/coarseConversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/coarseConversionValue). Earlier versions of SKAdNetwork use a single [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/conversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/conversionValue).

## See Also

- [fidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fidelityType.md)
- [fineConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fineConversionValue.md)
- [didWin](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/didWin.md)

---


### conversionvalue

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var conversionValue: Int { get }
```

## 

A postback in SKAdNetwork 3 or earlier uses a single [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/conversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/conversionValue). A postback in SKAdNetwork 4 or later may contain either a [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fineConversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fineConversionValue) or a [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/coarseConversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/coarseConversionValue).

## See Also

- [adCampaignIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adCampaignIdentifier.md)

---


### didwin

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var didWin: Bool { get }
```

## See Also

- [fidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fidelityType.md)
- [fineConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fineConversionValue.md)
- [coarseConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/coarseConversionValue.md)

---


### fidelitytype

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var fidelityType: Int { get set }
```

## 

SKAdNetwork versions 2.2 and later require a [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fidelityType](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fidelityType) parameter for ad validation signatures. For view-through ads, use a fidelity type value of `0`. For StoreKit-rendered ads, use the value `1`.

## See Also

- [fineConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fineConversionValue.md)
- [coarseConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/coarseConversionValue.md)
- [didWin](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/didWin.md)

---


### fineconversionvalue

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var fineConversionValue: Int { get }
```

## 

A postback in SKAdNetwork version 4 and later provides this [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fineConversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/fineConversionValue) or a [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/coarseConversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/coarseConversionValue). Earlier versions of SKAdNetwork use a single [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/conversionValue](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/conversionValue).

## See Also

- [fidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fidelityType.md)
- [coarseConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/coarseConversionValue.md)
- [didWin](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/didWin.md)

---


### init(version:adnetworkidentifier:adcampaignidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:conversionvalue:fidelitytype:isredownload:didwin:postbackurl:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
init?(version: SKAdTestPostbackVersion, adNetworkIdentifier: String, adCampaignIdentifier: Int, appStoreItemIdentifier: Int, sourceAppStoreItemIdentifier: Int, conversionValue: Int, fidelityType: Int, isRedownload: Bool, didWin: Bool, postbackURL: String)
```

## Parameters

- **version**: [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion), the SKAdNetwork version. For more information about versions, see [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).
- **adNetworkIdentifier**: Your ad network identifier. For the test environment, you may use any lowercased value. You must use the same value to verify the signature after you receive the postback on your server. Also, use the same ad network identifier in the `Info.plist` of the source app in the testing environment.
- **adCampaignIdentifier**: The campaign identifier associated with the ad.
- **appStoreItemIdentifier**: The App Store item identifier of the advertised app.
- **sourceAppStoreItemIdentifier**: The App Store item identifier of the app that displays the ad. This value is `0` in the testing environment.
- **conversionValue**: SKAdNetwork version 2.0 and later. An unsigned 6-bit value that the installed app provides by calling [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updateConversionValue(_:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updateConversionValue(_:)). Note: In the production environment, the conversion-value only appears in the postback if the installed app provides it, and if providing the parameter meets Apple’s privacy threshold.
- **fidelityType**: SKAdNetwork version 2.2 and later. A value of `0` indicates a view-through ad presentation; a value of `1` indicates a StoreKit-rendered ad.
- **isRedownload**: SKAdNetwork version 2.0 and later. A Boolean flag that in the production environment indicates that the customer redownloaded and reinstalled the app when the value is `true`.
- **didWin**: SKAdNetwork version 3.0 and later. A Boolean value that’s `true` if the ad network won the attribution, and `false` if the postback represents a qualifying ad impression that didn’t win the attribution.
- **postbackURL**: A URL on your server where you can receive test postbacks.

## 

Create one to six test postbacks to use for unit testing. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) to add the test postbacks to the test session.

## See Also

- [init(version:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:didWin:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:didWin:postbackURL:).md)
- [winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:).md)

---


### init(version:adnetworkidentifier:sourceidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:sourcedomain:fidelitytype:isredownload:didwin:postbackurl:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
init?(version: SKAdTestPostbackVersion, adNetworkIdentifier: String, sourceIdentifier: String, appStoreItemIdentifier: Int, sourceAppStoreItemIdentifier: Int, sourceDomain: String?, fidelityType: Int, isRedownload: Bool, didWin: Bool, postbackURL: String)
```

## Parameters

- **version**: [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion), the SKAdNetwork version. For more information about versions, see [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).
- **adNetworkIdentifier**: Your ad network identifier. For the test environment, you may use any lowercased value. You must use the same value to verify the signature after you receive the postback on your server. Also, use the same ad network identifier in the `Info.plist` of the source app in the testing environment.
- **sourceIdentifier**: Four digits that represent the ad campaign.
- **appStoreItemIdentifier**: The App Store item identifier of the advertised app.
- **sourceAppStoreItemIdentifier**: The App Store item identifier of the app that displays the ad. This value is `0` in the testing environment.
- **sourceDomain**: The domain of the website that displays the ad.
- **fidelityType**: A value of `0` indicates a view-through ad presentation; a value of `1` indicates a StoreKit-rendered ad or a web ad.
- **isRedownload**: In the production environment, a Boolean flag that indicates that the customer redownloaded and reinstalled the app when the value is `true`.
- **didWin**: A Boolean value that’s `true` if the ad network won the attribution, and `false` if the postback represents a qualifying ad impression that didn’t win the attribution.
- **postbackURL**: A URL on your server where you can receive test postbacks.

## See Also

- [winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:).md)
- [init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:).md)

---


### isredownload

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var isRedownload: Bool { get }
```

## 

In the production environment, this value is `true` when the user redownloaded and reinstalled the app. In the testing environment, you set the value of this property when you create the test postback.

## See Also

- [version](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/version.md)
- [transactionIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/transactionIdentifier.md)
- [postbackSequenceIndex](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/postbackSequenceIndex.md)
- [isRegistered](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRegistered.md)

---


### isregistered

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var isRegistered: Bool { get }
```

## 

To register a postback, call [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)), or [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()).

## See Also

- [version](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/version.md)
- [transactionIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/transactionIdentifier.md)
- [postbackSequenceIndex](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/postbackSequenceIndex.md)
- [isRedownload](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRedownload.md)

---


### postbacksequenceindex

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var postbackSequenceIndex: Int { get }
```

## 

For more information about receiving time-delayed postbacks for an ad impression, see [doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows](doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [version](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/version.md)
- [transactionIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/transactionIdentifier.md)
- [isRegistered](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRegistered.md)
- [isRedownload](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRedownload.md)

---


### postbackurl

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var postbackURL: String { get }
```

## 

The testing environment sends the test postback to the [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/postbackURL](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/postbackURL) when you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)).

> **NOTE:** Ensure that your test server is running and accepting connections before calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)).

---


### sourceappstoreitemidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var sourceAppStoreItemIdentifier: Int { get }
```

## 

In the testing environment, the [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier) is always `0`.

## See Also

- [adNetworkIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adNetworkIdentifier.md)
- [appStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/appStoreItemIdentifier.md)
- [sourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceDomain.md)
- [sourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceIdentifier.md)

---


### sourcedomain

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var sourceDomain: String? { get }
```

## 

This postback value indicates the `source_domain` of the corresponding [doc://com.apple.documentation/documentation/SKAdNetworkforWebAds/AdImpressionRequest](doc://com.apple.documentation/documentation/SKAdNetworkforWebAds/AdImpressionRequest).

## See Also

- [adNetworkIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adNetworkIdentifier.md)
- [appStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/appStoreItemIdentifier.md)
- [sourceAppStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier.md)
- [sourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceIdentifier.md)

---


### sourceidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var sourceIdentifier: String? { get }
```

## 

The source identifier in a winning postback may contain two, three, or all four digits of the [doc://com.apple.documentation/documentation/StoreKit/SKAdImpression/sourceIdentifier](doc://com.apple.documentation/documentation/StoreKit/SKAdImpression/sourceIdentifier) in the corresponding ad impression. For more information about the value you may get in the postback, see [doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows](doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [adNetworkIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adNetworkIdentifier.md)
- [appStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/appStoreItemIdentifier.md)
- [sourceAppStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier.md)
- [sourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceDomain.md)

---


### transactionidentifier

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var transactionIdentifier: String { get }
```

## 

The system generates this value when you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)). This value is an empty string otherwise.

Use this value to match the test postback with the response you receive from [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)).

## See Also

- [version](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/version.md)
- [postbackSequenceIndex](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/postbackSequenceIndex.md)
- [isRegistered](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRegistered.md)
- [isRedownload](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRedownload.md)

---


### version

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var version: SKAdTestPostbackVersion { get }
```

## 

For information about the SKAdNetwork versions, See [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).

## See Also

- [transactionIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/transactionIdentifier.md)
- [postbackSequenceIndex](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/postbackSequenceIndex.md)
- [isRegistered](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRegistered.md)
- [isRedownload](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRedownload.md)

---


### winningpostbacks(withversion:adnetworkidentifier:sourceidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:sourcedomain:fidelitytype:isredownload:postbackurl:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
class func winningPostbacks(withVersion version: SKAdTestPostbackVersion, adNetworkIdentifier: String, sourceIdentifier: String, appStoreItemIdentifier: Int, sourceAppStoreItemIdentifier: Int, sourceDomain: String?, fidelityType: Int, isRedownload: Bool, postbackURL: String) -> [SKAdTestPostback]?
```

## Parameters

- **version**: [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion), the SKAdNetwork version. For more information about versions, see [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).
- **adNetworkIdentifier**: Your ad network identifier. For the test environment, you may use any lowercased value. You must use the same value to verify the signature after you receive the postback on your server. Also, use the same ad network identifier in the `Info.plist` of the source app in the testing environment.
- **sourceIdentifier**: Four digits that represent the ad campaign.
- **appStoreItemIdentifier**: The App Store item identifier of the advertised app.
- **sourceAppStoreItemIdentifier**: The App Store item identifier of the app that displays the ad. This value is `0` in the testing environment.
- **sourceDomain**: The domain of the website that displays the ad.
- **fidelityType**: A value of `0` indicates a view-through ad presentation; a value of `1` indicates a StoreKit-rendered ad or a web ad.
- **isRedownload**: SKAdNetwork version 2.0 and later. In the production environment, a Boolean flag that indicates that the customer redownloaded and reinstalled the app when the value is `true`.
- **postbackURL**: A URL on your server where you can receive test postbacks.

## 

An array containing a winning postback for each conversion window.

## 

This method provides parameters to create test postbacks for either an in-app ad or a web ad. To create test postbacks for an in-app ad, provide an empty string for `sourceDomain`.

For more information about the conversion windows corresponding to each postback, see [doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows](doc://com.apple.documentation/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [init(version:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:didWin:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:didWin:postbackURL:).md)
- [init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:).md)

---


## skadtestpostbackresponse


### didsucceed

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var didSucceed: Bool { get set }
```

## 

The value is `true` if the system successfully delivered the test postback and received an HTTP 200 response.

## See Also

- [httpResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/httpResponse.md)
- [error](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/error.md)

---


### error

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var error: (any Error)? { get set }
```

## 

If the test session encounters an error when attempting to send the test postback with [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)), this property contains an [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError) error.

## See Also

- [didSucceed](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/didSucceed.md)
- [httpResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/httpResponse.md)

---


### httpresponse

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var httpResponse: HTTPURLResponse? { get set }
```

## 

This property contains your server’s full HTTP response.

## See Also

- [didSucceed](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/didSucceed.md)
- [error](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/error.md)

---


## skadtestpostbackversion


### version2_1

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static let version2_1: SKAdTestPostbackVersion
```

## See Also

- [version4_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version4_0.md)
- [version3_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version3_0.md)
- [version2_2](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_2.md)

---


### version2_2

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static let version2_2: SKAdTestPostbackVersion
```

## See Also

- [version4_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version4_0.md)
- [version3_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version3_0.md)
- [version2_1](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_1.md)

---


### version3_0

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static let version3_0: SKAdTestPostbackVersion
```

## See Also

- [version4_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version4_0.md)
- [version2_2](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_2.md)
- [version2_1](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_1.md)

---


### version4_0

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
static let version4_0: SKAdTestPostbackVersion
```

## See Also

- [version3_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version3_0.md)
- [version2_2](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_2.md)
- [version2_1](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_1.md)

---


## skadtestsession


### developerpostbackurl

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var developerPostbackURL: URL? { get }
```

## 

Use this property to view the URL that [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork) computes to send a copy of the winning postback to the developer. This property has a valid URL only if you specify a valid URL in the [doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint](doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint) key in your app’s `Info.plist`. For more information, see [doc://com.apple.documentation/documentation/StoreKit/configuring-an-advertised-app](doc://com.apple.documentation/documentation/StoreKit/configuring-an-advertised-app).

> **NOTE:** The testing environment doesn’t use this URL. [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork) sends copies of winning postbacks in the production environment only.

---


### flushpostbacks(responses:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
func flushPostbacks(responses: @escaping ([String : SKAdTestPostbackResponse]?, (any Error)?) -> Void)
```

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
func flushPostbacksWithResponses() async throws -> [String : SKAdTestPostbackResponse]
```

## Parameters

- **responses**: A handler that matches the signature of [doc://com.apple.storekittest/documentation/StoreKitTest/SKANTestPostbackResponseHandler](doc://com.apple.storekittest/documentation/StoreKitTest/SKANTestPostbackResponseHandler).

## 

This method sends the test postbacks that you set up using [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) to the server URL provided in each postback, and then deletes them from this test session. Note that you set up the postback server URL when you create the postback instance using [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback).

This method calls the response handler with either a dictionary that contains postback [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/transactionIdentifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/transactionIdentifier) keys with their responses ([doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackResponse](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackResponse)), or a single [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError) error. If you receive an error, it indicates a failure that isn’t specific to any single postback, but is a general issue; for example, a test session has no postbacks, there’s a connectivity issue, or the postbacks aren’t registered.

To perform tests with postbacks, do the following:

1. Create a test postback using [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback).
2. Add the test postbacks to the test session by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)).
3. In the code representing the advertised app, register the test postback by calling [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:))or [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()).
4. Optionally, update the conversion value by calling [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)).
5. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)) when you’re done updating the conversion value and are ready to test receiving postbacks on your server.

## See Also

- [setPostbacks(_:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/setPostbacks(_:).md)
- [postbacks](../com.apple.storekittest/StoreKitTest/SKAdTestSession/postbacks.md)
- [SKANTestPostbackResponseHandler](../com.apple.storekittest/StoreKitTest/SKANTestPostbackResponseHandler.md)

---


### init()

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
init()
```

## 

You can share a single instance of this class with multiple test cases.

---


### postbacks

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
var postbacks: [SKAdTestPostback] { get }
```

## 

Use this property to check that your updates to the test postbacks, such as conversion value updates, are working as expected. See [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) for information on adding postbacks to the test session.

## See Also

- [setPostbacks(_:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/setPostbacks(_:).md)
- [flushPostbacks(responses:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/flushPostbacks(responses:).md)
- [SKANTestPostbackResponseHandler](../com.apple.storekittest/StoreKitTest/SKANTestPostbackResponseHandler.md)

---


### setpostbacks(_:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
func setPostbacks(_ postbacks: [SKAdTestPostback]) throws
```

## Parameters

- **postbacks**: An array of one to six test postbacks you add to a test session. The first postback must always be the winning postback with a `didWin` value of `true`. There must be only one winning postback.

## 

An error occurs if any of the test postbacks are invalid or if there’s an issue with the set of test postbacks. Otherwise, the test passes.

Create postbacks using the initializer for [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback), [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)). Add the postbacks to the test session by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)).

Calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) overwrites previous postbacks in the test session, if any exist.

Include up to six test postbacks in your test session if you want to mimic the behavior of postbacks when users experience multiple ad impressions for the same app. For more information about attributions when there are multiple ad impressions, see [doc://com.apple.documentation/documentation/StoreKit/receiving-ad-attributions-and-postbacks](doc://com.apple.documentation/documentation/StoreKit/receiving-ad-attributions-and-postbacks).

The array of test postbacks in the test session need to follow the same rules that SKAdNetwork uses for postbacks, including:

- The `postbacks` array can only contain up to six postbacks.
- The first postback in the array must be the only winning postback in the array, with a `didWin` value of `true`.
- All postbacks, except the first postback in the array, have a `didWin` value of `false`.

## See Also

- [postbacks](../com.apple.storekittest/StoreKitTest/SKAdTestSession/postbacks.md)
- [flushPostbacks(responses:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/flushPostbacks(responses:).md)
- [SKANTestPostbackResponseHandler](../com.apple.storekittest/StoreKitTest/SKANTestPostbackResponseHandler.md)

---


### validate(_:publickey:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
func validate(_ impression: SKAdImpression, publicKey: String) throws
```

## Parameters

- **impression**: An [doc://com.apple.documentation/documentation/StoreKit/SKAdImpression](doc://com.apple.documentation/documentation/StoreKit/SKAdImpression) instance, representing your ad impression.
- **publicKey**: The public key of the elliptic curve cryptographic key pair you used to generate the signature for the ad impression.

## 

The cryptographic key pair you use for testing may be a different key pair than you use in production. For testing, use keys from the same key pair to sign the ad impression for testing and call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)).

For more information about signing ad impressions, see [doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads](doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads).

## See Also

- [validateImpression(parameters:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:).md)
- [validateWebAdImpressionPayload(_:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:).md)

---


### validateimpression(parameters:publickey:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
func validateImpression(parameters: [String : Any], publicKey: String) throws
```

## Parameters

- **parameters**: A dictionary containing version-specific key values that associate an app installation with an ad campaign for StoreKit-rendered ads. See [doc://com.apple.documentation/documentation/StoreKit/ad-network-install-validation-keys](doc://com.apple.documentation/documentation/StoreKit/ad-network-install-validation-keys) for the list of required keys.
- **publicKey**: The public key of the elliptic curve cryptographic key pair you used to generate the signature for the ad impression.

## 

The cryptographic key pair you use for testing may be a different key pair than you use in production. For testing, use keys from the same key pair when you sign the ad impression and when you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)).

For more information about signing ad impressions, see [doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads](doc://com.apple.documentation/documentation/StoreKit/signing-and-providing-ads).

## See Also

- [validate(_:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validate(_:publicKey:).md)
- [validateWebAdImpressionPayload(_:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:).md)

---


### validatewebadimpressionpayload(_:publickey:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
func validateWebAdImpressionPayload(_ impressionData: Data, publicKey: String) throws
```

## See Also

- [validate(_:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validate(_:publicKey:).md)
- [validateImpression(parameters:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:).md)

---


## sktestfailures


### purchase


#### purchase(_:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case purchase(Product.PurchaseError)
```

## See Also

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase/generic(_:).md)

---


### refundrequest


#### generic(_:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, visionOS

```swift
case generic(StoreKitError)
```

## See Also

- [refundRequest(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest/refundRequest(_:).md)

---


#### refundrequest(_:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, visionOS

```swift
case refundRequest(Transaction.RefundRequestError)
```

## See Also

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest/generic(_:).md)

---


### verification


#### verification(_:)

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
case verification(VerificationResult<Any>.VerificationError)
```

---


### appstoresync

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum AppStoreSync
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync/generic(_:).md)

## See Also

- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### apptransaction

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum AppTransaction
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction/generic(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### loadproducts

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum LoadProducts
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts/generic(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### managesubscriptions

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum ManageSubscriptions
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions/generic(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### offercoderedeem

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum OfferCodeRedeem
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem/generic(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### purchase

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum Purchase
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase/generic(_:).md)
- [purchase(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase/purchase(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### refundrequest

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, visionOS

```swift
enum RefundRequest
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest/generic(_:).md)
- [refundRequest(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest/refundRequest(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### subscriptionstatus

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum SubscriptionStatus
```

## Topics

### Enumeration Cases

- [generic(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus/generic(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


### verification

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum Verification
```

## Topics

### Enumeration Cases

- [verification(_:)](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification/verification(_:).md)

## See Also

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)

---


## SKAdTestError

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
struct SKAdTestError
```

## 

Unit tests that call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)), [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)), [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)), and [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)), can throw [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError) errors.

When you call the unit test methods [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)), [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)), or [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:)) to validate your ad impression, the system may return signature-related errors.

When you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) and [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)), you may get postback-related errors.

## Topics

### Getting Signature Errors

- [missingSignature](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingSignature.md)
- [signatureInvalidKey](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidKey.md)
- [signatureInvalidOrder](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureInvalidOrder.md)
- [signatureMissingAdNetworkId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAdNetworkId.md)
- [signatureMissingAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingAppAdamId.md)
- [signatureMissingFidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingFidelityType.md)
- [signatureMissingNonce](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingNonce.md)
- [signatureMissingSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceAppAdamId.md)
- [signatureMissingSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceDomain.md)
- [signatureMissingSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingSourceIdentifier.md)
- [signatureMissingTimestamp](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingTimestamp.md)
- [signatureUnknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureUnknownError.md)
- [signatureVerificationFailed](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureVerificationFailed.md)

### Getting Postback Errors

- [excessivePostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/excessivePostbacks.md)
- [invalidConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidConversionValue.md)
- [invalidPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidPostbackURL.md)
- [invalidRunnerUpPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidRunnerUpPostback.md)
- [invalidWinningPostbackCount](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidWinningPostbackCount.md)
- [malformedPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/malformedPostbacks.md)
- [missingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingPostbacks.md)
- [misplacedWinnerPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/misplacedWinnerPostback.md)
- [missingWinningPostback](../com.apple.storekittest/StoreKitTest/SKAdTestError/missingWinningPostback.md)
- [noPendingPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/noPendingPostbacks.md)
- [unlinkedWinningPostbacks](../com.apple.storekittest/StoreKitTest/SKAdTestError/unlinkedWinningPostbacks.md)

### Getting Other Errors

- [invalidVersion](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidVersion.md)
- [invalidImpressionId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidImpressionId.md)
- [invalidSourceAppAdamId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceAppAdamId.md)
- [invalidSourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceDomain.md)
- [invalidSourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidSourceIdentifier.md)
- [unknownError](../com.apple.storekittest/StoreKitTest/SKAdTestError/unknownError.md)

### Getting Older Errors

- [invalidCampaignId](../com.apple.storekittest/StoreKitTest/SKAdTestError/invalidCampaignId.md)
- [signatureMissingCampaignId](../com.apple.storekittest/StoreKitTest/SKAdTestError/signatureMissingCampaignId.md)
- [conflictingSource](../com.apple.storekittest/StoreKitTest/SKAdTestError/conflictingSource.md)

### Initializing the Error Objects

- [Code](../com.apple.storekittest/StoreKitTest/SKAdTestError/Code.md)

### Type Properties

- [errorDomain](../com.apple.storekittest/StoreKitTest/SKAdTestError/errorDomain.md)

## See Also

- [SKAdTestErrorDomain](../com.apple.storekittest/StoreKitTest/SKAdTestErrorDomain.md)

---


## SKAdTestPostback

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
class SKAdTestPostback
```

## 

Use this class to create test postbacks to use for unit testing.

In the production environment, the system creates a postback after a user installs an advertised app. The advertised app is responsible for registering the installation and may update the conversion value. The system sends the postback after a timer expires.

In the testing environment, you can mimic a postback by creating it directly. You control the property values within the postback. Use it to test your app’s ability to register the app installation and update conversion values, and to test your server’s ability to receive postbacks.

## Topics

### Creating test postbacks

- [init(version:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:didWin:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:didWin:postbackURL:).md)
- [winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:).md)
- [init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:).md)

### Getting the Postback Destination

- [postbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/postbackURL.md)

### Getting general information

- [version](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/version.md)
- [transactionIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/transactionIdentifier.md)
- [postbackSequenceIndex](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/postbackSequenceIndex.md)
- [isRegistered](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRegistered.md)
- [isRedownload](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/isRedownload.md)

### Getting advertisement information

- [adNetworkIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adNetworkIdentifier.md)
- [appStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/appStoreItemIdentifier.md)
- [sourceAppStoreItemIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceAppStoreItemIdentifier.md)
- [sourceDomain](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceDomain.md)
- [sourceIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/sourceIdentifier.md)

### Getting conversion information

- [fidelityType](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fidelityType.md)
- [fineConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/fineConversionValue.md)
- [coarseConversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/coarseConversionValue.md)
- [didWin](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/didWin.md)

### Getting information in earlier versions

- [adCampaignIdentifier](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/adCampaignIdentifier.md)
- [conversionValue](../com.apple.storekittest/StoreKitTest/SKAdTestPostback/conversionValue.md)

## See Also

- [testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork](../com.apple.storekittest/StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
- [SKAdTestSession](../com.apple.storekittest/StoreKitTest/SKAdTestSession.md)
- [SKAdTestPostbackResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse.md)
- [SKAdTestPostbackVersion](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion.md)

---


## SKTestError

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct SKTestError
```

## Topics

### Error Domain

- [errorDomain](../com.apple.storekittest/StoreKitTest/SKTestError/errorDomain.md)

### Error Codes

- [fileNotFound](../com.apple.storekittest/StoreKitTest/SKTestError/fileNotFound.md)
- [invalidAction](../com.apple.storekittest/StoreKitTest/SKTestError/invalidAction.md)
- [invalidProductIdentifier](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductIdentifier.md)
- [invalidProductType](../com.apple.storekittest/StoreKitTest/SKTestError/invalidProductType.md)
- [invalidURL](../com.apple.storekittest/StoreKitTest/SKTestError/invalidURL.md)
- [noSubscriptionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noSubscriptionFound.md)
- [noTransactionFound](../com.apple.storekittest/StoreKitTest/SKTestError/noTransactionFound.md)
- [serviceUnavailable](../com.apple.storekittest/StoreKitTest/SKTestError/serviceUnavailable.md)
- [Code](../com.apple.storekittest/StoreKitTest/SKTestError/Code.md)

## See Also

- [SKTestErrorDomain](../com.apple.storekittest/StoreKitTest/SKTestErrorDomain.md)

---


## SKTestFailure

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
protocol SKTestFailure : Equatable, Sendable
```

## See Also

- [FailableStoreKitAPI](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI.md)

---


## SKTestFailures

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
enum SKTestFailures
```

## Topics

### Enumerations

- [AppStoreSync](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppStoreSync.md)
- [AppTransaction](../com.apple.storekittest/StoreKitTest/SKTestFailures/AppTransaction.md)
- [LoadProducts](../com.apple.storekittest/StoreKitTest/SKTestFailures/LoadProducts.md)
- [ManageSubscriptions](../com.apple.storekittest/StoreKitTest/SKTestFailures/ManageSubscriptions.md)
- [OfferCodeRedeem](../com.apple.storekittest/StoreKitTest/SKTestFailures/OfferCodeRedeem.md)
- [Purchase](../com.apple.storekittest/StoreKitTest/SKTestFailures/Purchase.md)
- [RefundRequest](../com.apple.storekittest/StoreKitTest/SKTestFailures/RefundRequest.md)
- [SubscriptionStatus](../com.apple.storekittest/StoreKitTest/SKTestFailures/SubscriptionStatus.md)
- [Verification](../com.apple.storekittest/StoreKitTest/SKTestFailures/Verification.md)

---


## SKTestSession

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
class SKTestSession
```

## 

This class controls the settings that the server uses when it processes transactions. Run tests that reconfigure the environment serially, not concurrently, to avoid overwriting each other’s environment settings.

> **NOTE:** There’s a single instance of the test environment. All `SKTestSession` instances control the same test environment.

The test environment creates an [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestTransaction) instance each time your test code calls any method of `SKTestSession` that affects in-app purchases, including:

- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/buyProduct(productIdentifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/buyProduct(productIdentifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/refundTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/refundTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:))
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:))

You can manage the transactions in the test environment. To get a list of all transactions in the test environment, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/allTransactions()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/allTransactions()). To delete a single transaction, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/deleteTransaction(identifier:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/deleteTransaction(identifier:)). To delete all the transactions, call [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/clearTransactions()](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/clearTransactions()).

Before automating a test session with `SKTestSession`, you must create a StoreKit configuration file. For more information, see [doc://com.apple.documentation/documentation/Xcode/setting-up-storekit-testing-in-xcode](doc://com.apple.documentation/documentation/Xcode/setting-up-storekit-testing-in-xcode) and [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/init(configurationFileNamed:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/init(configurationFileNamed:)). Set [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession/disableDialogs) to `true` to run tests without showing test environment UI.

## Topics

### Initializing test sessions

- [init(configurationFileNamed:)](../com.apple.storekittest/StoreKitTest/SKTestSession/init(configurationFileNamed:).md)
- [init(contentsOf:)](../com.apple.storekittest/StoreKitTest/SKTestSession/init(contentsOf:).md)
- [resetToDefaultState()](../com.apple.storekittest/StoreKitTest/SKTestSession/resetToDefaultState().md)

### Configuring the test environment

- [storefront](../com.apple.storekittest/StoreKitTest/SKTestSession/storefront.md)
- [locale](../com.apple.storekittest/StoreKitTest/SKTestSession/locale.md)
- [disableDialogs](../com.apple.storekittest/StoreKitTest/SKTestSession/disableDialogs.md)

### Managing transactions in the test environment

- [allTransactions()](../com.apple.storekittest/StoreKitTest/SKTestSession/allTransactions().md)
- [deleteTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/deleteTransaction(identifier:).md)
- [clearTransactions()](../com.apple.storekittest/StoreKitTest/SKTestSession/clearTransactions().md)

### Forcing failed transactions

- [failTransactionsEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/failTransactionsEnabled.md)
- [failureError](../com.apple.storekittest/StoreKitTest/SKTestSession/failureError.md)

### Testing interrupted purchases

- [interruptedPurchasesEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/interruptedPurchasesEnabled.md)
- [resolveIssueForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:).md)

### Testing Ask To Buy transactions

- [askToBuyEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/askToBuyEnabled.md)
- [approveAskToBuyTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/approveAskToBuyTransaction(identifier:).md)
- [declineAskToBuyTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/declineAskToBuyTransaction(identifier:).md)

### Testing subscription renewals

- [timeRate-swift.property](../com.apple.storekittest/StoreKitTest/SKTestSession/timeRate-swift.property.md)
- [TimeRate-swift.enum](../com.apple.storekittest/StoreKitTest/SKTestSession/TimeRate-swift.enum.md)
- [enableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/enableAutoRenewForTransaction(identifier:).md)
- [disableAutoRenewForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/disableAutoRenewForTransaction(identifier:).md)
- [forceRenewalOfSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/forceRenewalOfSubscription(productIdentifier:).md)
- [expireSubscription(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/expireSubscription(productIdentifier:).md)

### Testing billing retry and grace period

- [billingGracePeriodIsEnabled](../com.apple.storekittest/StoreKitTest/SKTestSession/billingGracePeriodIsEnabled.md)
- [shouldEnterBillingRetryOnRenewal](../com.apple.storekittest/StoreKitTest/SKTestSession/shouldEnterBillingRetryOnRenewal.md)
- [resolveIssueForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/resolveIssueForTransaction(identifier:).md)

### Testing price increase consent

- [requestPriceIncreaseConsentForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/requestPriceIncreaseConsentForTransaction(identifier:).md)
- [consentToPriceIncreaseForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/consentToPriceIncreaseForTransaction(identifier:).md)
- [declinePriceIncreaseForTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/declinePriceIncreaseForTransaction(identifier:).md)

### Testing externally performed transactions

- [buyProduct(productIdentifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/buyProduct(productIdentifier:).md)
- [refundTransaction(identifier:)](../com.apple.storekittest/StoreKitTest/SKTestSession/refundTransaction(identifier:).md)

### Instance Methods

- [buyProduct(identifier:options:)](../com.apple.storekittest/StoreKitTest/SKTestSession/buyProduct(identifier:options:).md)
- [setSimulatedError(_:forAPI:)](../com.apple.storekittest/StoreKitTest/SKTestSession/setSimulatedError(_:forAPI:).md)
- [simulatedError(forAPI:)](../com.apple.storekittest/StoreKitTest/SKTestSession/simulatedError(forAPI:).md)

## See Also

- [setting-up-storekit-testing-in-xcode](../com.apple.Xcode/setting-up-storekit-testing-in-xcode.md)
- [SKTestTransaction](../com.apple.storekittest/StoreKitTest/SKTestTransaction.md)

---


## StoreKitAppStoreSyncAPI

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitAppStoreSyncAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI/init().md)

## See Also

- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## StoreKitManageSubscriptionsAPI

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitManageSubscriptionsAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## StoreKitOfferCodeRedeemAPI

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitOfferCodeRedeemAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## StoreKitPurchaseAPI

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitPurchaseAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## StoreKitRefundRequestAPI

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, visionOS

```swift
struct StoreKitRefundRequestAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## StoreKitSubscriptionStatusAPI

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitSubscriptionStatusAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## failablestorekitapi

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
protocol FailableStoreKitAPI<Failure> : Sendable
```

## Topics

### Associated Types

- [Failure](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/Failure.md)

### Type Properties

- [appStoreSync](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/appStoreSync.md)
- [appTransaction](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/appTransaction.md)
- [loadProducts](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/loadProducts.md)
- [manageSubscriptions](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/manageSubscriptions.md)
- [offerCodeRedeem](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/offerCodeRedeem.md)
- [purchase](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/purchase.md)
- [refundRequest](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/refundRequest.md)
- [subscriptionStatus](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/subscriptionStatus.md)
- [verification](../com.apple.storekittest/StoreKitTest/FailableStoreKitAPI/verification.md)

## See Also

- [SKTestFailure](../com.apple.storekittest/StoreKitTest/SKTestFailure.md)

---


## skadtesterrordomain

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, visionOS

```swift
let SKAdTestErrorDomain: String
```

## See Also

- [SKAdTestError](../com.apple.storekittest/StoreKitTest/SKAdTestError.md)

---


## skadtestpostbackresponse

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
class SKAdTestPostbackResponse
```

## Topics

### Getting Postback Responses

- [didSucceed](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/didSucceed.md)
- [httpResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/httpResponse.md)
- [error](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse/error.md)

## See Also

- [testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork](../com.apple.storekittest/StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
- [SKAdTestSession](../com.apple.storekittest/StoreKitTest/SKAdTestSession.md)
- [SKAdTestPostback](../com.apple.storekittest/StoreKitTest/SKAdTestPostback.md)
- [SKAdTestPostbackVersion](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion.md)

---


## skadtestpostbackversion

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
struct SKAdTestPostbackVersion
```

## 

This postback version number corresponds to a version of SKAdNetwork. All versions of [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork) have specific instructions for signing ads and validating postbacks. The testing environment supports testing the versions indicated by the constants listed in the Getting SKAdNetwork Versions section below.

For more information about versions, see [doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes](doc://com.apple.documentation/documentation/StoreKit/skadnetwork-release-notes).

## Topics

### Getting SKAdNetwork Versions

- [version4_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version4_0.md)
- [version3_0](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version3_0.md)
- [version2_2](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_2.md)
- [version2_1](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/version2_1.md)

### Initializing the Postback Version

- [init(rawValue:)](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion/init(rawValue:).md)

## See Also

- [testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork](../com.apple.storekittest/StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
- [SKAdTestSession](../com.apple.storekittest/StoreKitTest/SKAdTestSession.md)
- [SKAdTestPostback](../com.apple.storekittest/StoreKitTest/SKAdTestPostback.md)
- [SKAdTestPostbackResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse.md)

---


## skadtestsession

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
class SKAdTestSession
```

## 

Use the `SKAdTestSession` class to test your implementations of SKAdNetwork. Create one instance of this class to use in multiple test cases. The instance represents a test session, and holds a set of test postbacks. Use [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback) to create test postbacks. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)) to add test postbacks to the test session. The test session deletes the postbacks from the instance after you call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)).

> **NOTE:** Check [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackVersion) for the list of SKAdNetwork versions that the testing environment supports.

### 

In the production environment, ad networks sign the ad impressions that apps display. In the testing environment, you have the opportunity to validate the ad impression signature. Ad networks provide two types of ads: StoreKit-rendered ads and view-through ads. To validate the ad impressions, use the following methods:

- [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validate(_:publicKey:)) to test your signature for view-through ads
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:)) to test your signature for StoreKit-rendered ads
- [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:)) to test your signature for web ads

You need a cryptographic private key to generate signatures. Use a public/private key pair that you create using an Elliptic Curve Digital Signature Algorithm (ECDSA) with a prime256V1 curve. Provide the public key in the validation methods. Secure your private keys as you would other credentials, such as passwords. Never share your private keys, store keys in a code repository, or include keys in client-facing code.

### 

In the production environment, ad networks receive postbacks on their server after users install an advertised app and a timer expires. In the testing environment, you can control all aspects of the postback, including when it’s sent.

In the production environment, an advertised app may update a conversion value as the user interacts with the app. The final conversion value appears in the winning postback. In the testing environment, you have the opportunity to check the test postback before it’s sent to determine whether your app is updating conversion values as expected.

To perform tests on conversion values and postbacks, follow these steps:

1. Create up to six test postbacks using [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback).
2. Add the test postbacks to the test session by calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/setPostbacks(_:)).
3. In the code representing the advertised app, register the test postbacks by calling [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:))or [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/registerAppForAdNetworkAttribution()).
4. To test conversion values, call [doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)](doc://com.apple.documentation/documentation/StoreKit/SKAdNetwork/updatePostbackConversionValue(_:completionHandler:)) to update the conversion value of the winning test postback.
5. Call [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)) when you’re done updating the conversion value and are ready to test receiving postbacks on your server. This method sends the test postbacks to your server, and removes them from the test session.

## Topics

### Validating impressions

- [validate(_:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validate(_:publicKey:).md)
- [validateImpression(parameters:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validateImpression(parameters:publicKey:).md)
- [validateWebAdImpressionPayload(_:publicKey:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/validateWebAdImpressionPayload(_:publicKey:).md)

### Adding and sending postbacks

- [setPostbacks(_:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/setPostbacks(_:).md)
- [postbacks](../com.apple.storekittest/StoreKitTest/SKAdTestSession/postbacks.md)
- [flushPostbacks(responses:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/flushPostbacks(responses:).md)
- [SKANTestPostbackResponseHandler](../com.apple.storekittest/StoreKitTest/SKANTestPostbackResponseHandler.md)

### Viewing the developer postback URL

- [developerPostbackURL](../com.apple.storekittest/StoreKitTest/SKAdTestSession/developerPostbackURL.md)

### Initializing test sessions

- [init()](../com.apple.storekittest/StoreKitTest/SKAdTestSession/init().md)

## See Also

- [testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork](../com.apple.storekittest/StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
- [SKAdTestPostback](../com.apple.storekittest/StoreKitTest/SKAdTestPostback.md)
- [SKAdTestPostbackResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse.md)
- [SKAdTestPostbackVersion](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion.md)

---


## skantestpostbackresponsehandler

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst

```swift
typealias SKANTestPostbackResponseHandler = ([String : SKAdTestPostbackResponse]?, (any Error)?) -> Void
```

## 

The system calls the response handler and provides one of two values:

- A dictionary with a key that identifies a test postback using its [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/transactionIdentifier](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback/transactionIdentifier) value, and the associated value of the response, [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackResponse](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackResponse) that you receive when calling [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:)](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession/flushPostbacks(responses:))
- An [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestError) error

## See Also

- [setPostbacks(_:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/setPostbacks(_:).md)
- [postbacks](../com.apple.storekittest/StoreKitTest/SKAdTestSession/postbacks.md)
- [flushPostbacks(responses:)](../com.apple.storekittest/StoreKitTest/SKAdTestSession/flushPostbacks(responses:).md)

---


## sktesterrordomain

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
let SKTestErrorDomain: String
```

## See Also

- [SKTestError](../com.apple.storekittest/StoreKitTest/SKTestError.md)

---


## sktesttransaction

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
class SKTestTransaction
```

## 

The test transaction represents the test environment’s knowledge of the transaction, including its identifier and the transaction’s state. It represents all the transaction-related configurations you control manually in Xcode for interrupted purchases, Ask to Buy scenarios, and changes to a subscription’s auto-renew state.

The test environment creates an `SKTestTransaction` instance each time your test code calls any method of [doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKTestSession) that affects in-app purchases.

## Topics

### Identifying Transactions and Products

- [identifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/identifier.md)
- [originalTransactionIdentifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/originalTransactionIdentifier.md)
- [productIdentifier](../com.apple.storekittest/StoreKitTest/SKTestTransaction/productIdentifier.md)

### Getting Payment Transaction States

- [state](../com.apple.storekittest/StoreKitTest/SKTestTransaction/state.md)

### Getting Dates

- [purchaseDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/purchaseDate.md)
- [cancelDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/cancelDate.md)
- [expirationDate](../com.apple.storekittest/StoreKitTest/SKTestTransaction/expirationDate.md)

### Getting Test Environment States

- [autoRenewingEnabled](../com.apple.storekittest/StoreKitTest/SKTestTransaction/autoRenewingEnabled.md)
- [hasPurchaseIssue](../com.apple.storekittest/StoreKitTest/SKTestTransaction/hasPurchaseIssue.md)
- [isPendingPriceIncreaseConsent](../com.apple.storekittest/StoreKitTest/SKTestTransaction/isPendingPriceIncreaseConsent.md)
- [pendingAskToBuyConfirmation](../com.apple.storekittest/StoreKitTest/SKTestTransaction/pendingAskToBuyConfirmation.md)

## See Also

- [setting-up-storekit-testing-in-xcode](../com.apple.Xcode/setting-up-storekit-testing-in-xcode.md)
- [SKTestSession](../com.apple.storekittest/StoreKitTest/SKTestSession.md)

---


## storekitapptransactionapi

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitAppTransactionAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## storekitloadproductsapi

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitLoadProductsAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)
- [StoreKitVerificationAPI](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI.md)

---


## storekitverificationapi

## Declaration

**Platforms:** iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS

```swift
struct StoreKitVerificationAPI
```

## Topics

### Initializers

- [init()](../com.apple.storekittest/StoreKitTest/StoreKitVerificationAPI/init().md)

## See Also

- [StoreKitAppStoreSyncAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppStoreSyncAPI.md)
- [StoreKitAppTransactionAPI](../com.apple.storekittest/StoreKitTest/StoreKitAppTransactionAPI.md)
- [StoreKitLoadProductsAPI](../com.apple.storekittest/StoreKitTest/StoreKitLoadProductsAPI.md)
- [StoreKitManageSubscriptionsAPI](../com.apple.storekittest/StoreKitTest/StoreKitManageSubscriptionsAPI.md)
- [StoreKitOfferCodeRedeemAPI](../com.apple.storekittest/StoreKitTest/StoreKitOfferCodeRedeemAPI.md)
- [StoreKitPurchaseAPI](../com.apple.storekittest/StoreKitTest/StoreKitPurchaseAPI.md)
- [StoreKitRefundRequestAPI](../com.apple.storekittest/StoreKitTest/StoreKitRefundRequestAPI.md)
- [StoreKitSubscriptionStatusAPI](../com.apple.storekittest/StoreKitTest/StoreKitSubscriptionStatusAPI.md)

---


## testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork

## 

This sample code project provides examples of how to use the StoreKit Test framework to test individual units of an [https://developer.apple.com/documentation/storekit/skadnetwork](https://developer.apple.com/documentation/storekit/skadnetwork) implementation. The sample code runs each type of test that [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession) makes possible.

First, it creates and validates ad impressions. In a typical ad attribution flow, the ad network cryptographically signs an ad impression. This unit test checks the signature and validates other aspects of the impression.

Next, the sample code creates a test postback and updates the conversion value. In a typical ad attribution flow, the system creates a postback after a user installs and opens an advertised app. In the unit test, you can see and control every aspect of the test postback, so you can test your app’s conversion values and decide which postback to annotate as the winner.

Finally, the sample code sends and receives the test postbacks. In a typical ad attribution flow, the system sends a postback after a timer expires. In the unit test, you control when to send the postback so that you can test that your server receives the postback.

### 

To run the unit tests in your environment with your settings, you’ll need the following:

- Your ad network identifier. Configure the value in your `Info.plist` as described in [https://developer.apple.com/documentation/storekit/skadnetwork/configuring_a_source_app](https://developer.apple.com/documentation/storekit/skadnetwork/configuring_a_source_app). In the sample code, use the same value everywhere that the ad network identifier is required.
- A source app identifier. In the testing environment, this value is always `0`.
- A cryptographic key pair, consisting of a public key and a private key, created with the Elliptic Curve Digital Signature Algorithm (ECDSA) with a `prime256v1` curve. In the sample code, use the private key when you generate a signature, and use the public key when you call `validateImpression`. - Set the `publicKey` variable in the sample code project to your public key.
- For more information on generating a private and public key pair for signing ads, visit [https://developer.apple.com/documentation/storekit/skadnetwork/registering_an_ad_network](https://developer.apple.com/documentation/storekit/skadnetwork/registering_an_ad_network).
- A local or remote server to listen for postbacks. Specify your server’s URL when you create test postbacks as shown in the sample code’s `testAddingPostbacks()` method.
- A device running iOS 16.4 or later. iOS Simulator doesn’t support [skadnetwork_linkid](skadnetwork_linkid).

### 

In the `testImpressionValidity()` method, the unit test creates an instance of [https://developer.apple.com/documentation/storekit/skadimpression](https://developer.apple.com/documentation/storekit/skadimpression) to represent a view-through ad.

All of the properties are required. In the testing environment, the [https://developer.apple.com/documentation/storekit/skadimpression/3727300-sourceappstoreitemidentifier](https://developer.apple.com/documentation/storekit/skadimpression/3727300-sourceappstoreitemidentifier) is always `0`.

```swift
// Form the SKAdImpression instance and configure it.
let impression = SKAdImpression()
impression.version = "4.0"
impression.adNetworkIdentifier = "com.apple.test-1"
impression.sourceIdentifier = 3120
impression.advertisedAppStoreItemIdentifier = 525_463_029
impression.adImpressionIdentifier = "b7c9da2b-15c7-4f3b-9326-135f9630033d"
impression.sourceAppStoreItemIdentifier = 0
impression.timestamp = 1_676_057_605_705
impression.signature = "MEQCIAtBBiadCFlMOEOh3K43xyKaU1/sj/CtgDOB+Wm7J+29AiBDfreX67mm4X9ZoM4xkHHLtuMM2OXcS5kQ7UpVb69A/Q=="
```

The unit test then calls the `validateImpression` method on [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestSession) and checks for errors.

If `validateImpression` returns an error, the unit test fails, and the error contains further information. If `validateImpression` doesn’t return an error, the unit test succeeds.

In the `testImpressionParametersValidity` method, the unit test creates a dictionary containing the parameters for a StoreKit-rendered ad and validates it using the `validateImpressionWithParameters` method. For more information about StoreKit-rendered ads, visit [https://developer.apple.com/documentation/storekit/skadnetwork/signing_and_providing_ads#3732910](https://developer.apple.com/documentation/storekit/skadnetwork/signing_and_providing_ads#3732910). The `testWebAdImpressionPayloadValidity` method creates and validates a web ad impression payload. For more information on web ads, visit [https://developer.apple.com/documentation/skadnetworkforwebads/get_a_signed_web_ad_impression_payload](https://developer.apple.com/documentation/skadnetworkforwebads/get_a_signed_web_ad_impression_payload).

> **NOTE:** For signature verification to succeed, provide the validate impression methods with the public key of the key pair used to generate the cryptographic signature for the ad impression.

### 

The unit test creates three winning postbacks in the `testAddingPostbacks` method using the [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostback) class. The fields of a postback are specific to each version of the [https://developer.apple.com/documentation/storekit/skadnetwork](https://developer.apple.com/documentation/storekit/skadnetwork) API. This class provides an initializer that specifies the postback fields and the `SKAdNetwork` API version.

For ad postbacks using `SKAdNetwork` version 4.0 or later, test multiple conversion windows by creating an array of three postbacks corresponding to the three conversion windows using the `winningPostbacks` static method on `SKAdTestPostback`. Create a single winning or nonwinning postback using the initializer with the `sourceIdentifier` parameter. For more information on multiple conversion windows, visit [https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows).

```swift
guard let testPostbacks = SKAdTestPostback.winningPostbacks(withVersion: .version4_0,
                                                            adNetworkIdentifier: "com.apple.test-1",
                                                            sourceIdentifier: "3120",
                                                            appStoreItemIdentifier: 0,
                                                            sourceAppStoreItemIdentifier: 525_463_029,
                                                            sourceDomain: nil,
                                                            fidelityType: 1,
                                                            isRedownload: false,
                                                            postbackURL: "TEST SERVER ENDPOINT") else {
    XCTFail("Failed to create postbacks.")
    return
}
```

After creating the `SKAdTestPostback` instances, the unit test calls the `setPostbacks` method on `SKAdTestSession` to add the newly created postbacks to the test session. Test postbacks added to the test session are available to the unit tests for further testing, including updating the conversion value or sending the postbacks. Test sessions can handle up to eight postbacks. Each call to the `setPostbacks` method overwrites the test postbacks in the test session.

```swift
try testSession.setPostbacks(testPostbacks)
```

### 

A postback isn’t ready to send to the server until it has a conversion value. The unit test updates the conversion value of the first test postback by calling the [https://developer.apple.com/documentation/storekit/skadnetwork/4090669-updatepostbackconversionvalue](https://developer.apple.com/documentation/storekit/skadnetwork/4090669-updatepostbackconversionvalue) method on [https://developer.apple.com/documentation/storekit/skadnetwork](https://developer.apple.com/documentation/storekit/skadnetwork). To confirm the conversion value after updating it, the unit test retrieves the postbacks using the `postbacks` property on `SKAdTestSession` and then checks the conversion value.

```swift
let fetchedPostbacks = testSession.postbacks
guard fetchedPostbacks.count == 3 else {
    XCTFail("Expecting 3 postbacks, received \(fetchedPostbacks.count).")
    return
}

// A test session's `postbacks` property maintains the order of the postbacks.
let firstPostback = fetchedPostbacks[0]
XCTAssertEqual(firstPostback.fineConversionValue, 42)
```

### 

The unit test sends the postbacks with updated conversion values to the network server by calling the `flushPostbacks` method on `SKAdTestSession` The server URL is specified in the `testAddingPostbacks` method, where the test postbacks are created.

> **IMPORTANT:** Before attempting to send postbacks using the `flushPostbacks` method, check that the specified test server is running and accepting connections.

After sending the test postbacks, the unit test waits for a response from the server. The server responds with one [doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackResponse](doc://com.apple.storekittest/documentation/StoreKitTest/SKAdTestPostbackResponse) instance for each test postback. The response contains information about the success or failure of the postback, the error details, and the HTTP response the server received, if any.

In the `testSendingPostback()` method, the unit test checks the response for the success or failure flag and the error object. The unit test passes only if it receives a success signal in combination with a `nil` error. Calling the `flushPostbacks` method removes the test postbacks from the test session.

```swift
testSession.flushPostbacks { responses, error in
    XCTAssertNil(error)
    guard let concreteResponses = responses else {
        XCTFail("No responses received.")
        return
    }
    for response in concreteResponses {
        let postbackResponse = response.value
        XCTAssertNil(postbackResponse.error)
        XCTAssertTrue(postbackResponse.didSucceed)
    }
}
```

## See Also

- [SKAdTestSession](../com.apple.storekittest/StoreKitTest/SKAdTestSession.md)
- [SKAdTestPostback](../com.apple.storekittest/StoreKitTest/SKAdTestPostback.md)
- [SKAdTestPostbackResponse](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackResponse.md)
- [SKAdTestPostbackVersion](../com.apple.storekittest/StoreKitTest/SKAdTestPostbackVersion.md)

---

