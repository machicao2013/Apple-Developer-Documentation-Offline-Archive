# appstoreservernotifications

*Merged documentation for appstoreservernotifications*

---

# App Store Server Notifications

## 

App Store Server Notifications is a server-to-server service that sends real-time notifications for In-App Purchase events, and notifications for unreported external purchase tokens. Use the data in the notifications to update your user-account database, and to monitor and respond to in-app purchase refunds. For notifications related to the [doc://com.apple.documentation/documentation/StoreKit/external-purchase](doc://com.apple.documentation/documentation/StoreKit/external-purchase) API, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken).

> **IMPORTANT:** The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint and version 1 notifications, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type), are deprecated. Implement the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications instead.

To receive server notifications from the App Store, provide your server’s HTTPS URL in App Store Connect. Opt in to receive notifications for the production environment and the sandbox environment. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).

Your server is responsible for parsing, interpreting, and responding to all server-to-server notification posts. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/receiving-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/receiving-app-store-server-notifications) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

### 

Notifications cover events in the in-app purchase life cycle, including purchases, subscription renewals, offer redemptions, refunds, and more. For a complete list of notification types, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) for [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2).

Use the notification type, along with the transaction and subscription renewal information, to update a customer’s service or to present promotional offers according to your business logic.

### 

A [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) of `EXTERNAL_PURCHASE_TOKEN` with an `UNREPORTED` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype) indicates that Apple generated an external purchase token for your app but hasn’t received a report for the token. The notification includes the token in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken) field of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). Use the token information to report it to Apple, including if you don’t recognize the token in your system. To report tokens, with or without associated transactions, call the [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI)’s [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint.

For more information about token reporting requirements, see [https://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/](https://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/).

### 

To determine whether your server is receiving notifications, call the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI) to ask the App Store server to send a notification with the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) `TEST`. Use the `testNotificationToken` you receive to call the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Test-Notification-Status) endpoint to learn how your server responds to the test notification.

The App Store server sends the `TEST` notification in the version 2 notification format, however, it sends it to your server regardless of whether you configure a version 1 or version 2 notification URL in App Store Connect. For more information about configuring your URL in App Store Connect, see [https://help.apple.com/app-store-connect/#/dev0067a330b](https://help.apple.com/app-store-connect/#/dev0067a330b).

## Topics

### Essentials

- [enabling-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/enabling-app-store-server-notifications.md)
- [receiving-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/receiving-app-store-server-notifications.md)
- [responding-to-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responding-to-app-store-server-notifications.md)
- [app-store-server-notifications-changelog](../com.apple.appstoreservernotifications/AppStoreServerNotifications/app-store-server-notifications-changelog.md)

### Server notifications version 2

- [App-Store-Server-Notifications-V2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V2.md)
- [responseBodyV2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2.md)
- [responseBodyV2DecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2DecodedPayload.md)
- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)

### Deprecated

- [app-store-server-notifications-version-1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/app-store-server-notifications-version-1.md)

## See Also

- [in-app-purchase](../com.apple.StoreKit/in-app-purchase.md)
- [AppStoreServerAPI](../com.apple.AppStoreServerAPI.md)
- [AppStoreReceipts](../com.apple.AppStoreReceipts.md)

---


# Detailed Documentation


## unified_receipt


### Latest_receipt_info-data.dictionary

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object unified_receipt.Latest_receipt_info
```

## See Also

- [Pending_renewal_info-data.dictionary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/unified_receipt/Pending_renewal_info-data.dictionary.md)

---


### pending_renewal_info-data.dictionary

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object unified_receipt.Pending_renewal_info
```

## See Also

- [Latest_receipt_info-data.dictionary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary.md)

---


## App-Store-Server-Notifications-V1

## 

To receive server notifications from the App Store, provide your secure server’s HTTPS URL in App Store Connect. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). To secure your server and receive notifications, your server must support the Transport Layer Security (TLS) protocol version 1.2 or later.

Upon receiving a server notification, respond to the App Store with an HTTP status code of `200` if the post was successful. If the post was unsuccessful, send HTTP `50x` or `40x` to have the App Store retry the notification. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

> **NOTE:** For version 2 notifications, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2).

## See Also

- [responseBodyV1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV1.md)
- [notification_type](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notification_type.md)

---


## JWSDecodedHeader

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object JWSDecodedHeader
```

## 

All JWS representations, including the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/signedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/signedPayload), contain a JWS header. When you Base64 URL-decode the header, use the [doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSDecodedHeader](doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSDecodedHeader) object to read its contents. Use the information in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader) to validate the JWS signature. For more information about validating signatures, see the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The App Store signs transaction and renewal information that you receive in [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) and in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI). It uses the following `x5c` certificate chain, in the following order:

1. A certificate that contains the public key that corresponds to the key the App Store uses to digitally sign the JWS. Section 4.11.10 Mac App Store Receipt Signing Certificates of the [https://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf](https://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf) document defines the custom extensions this certificate uses.
2. An Apple intermediate certificate that contains an extension with the extension ID for `Apple Worldwide Developer Relations (1.2.840.113635.100.6.2.1)`.
3. An Apple root certificate.

For more information, or to download Apple’s root and intermediate certificates, see [https://www.apple.com/certificateauthority/](https://www.apple.com/certificateauthority/).

## Topics

### JWS header types

- [alg](../com.apple.appstoreservernotifications/AppStoreServerNotifications/alg.md)
- [x5c](../com.apple.appstoreservernotifications/AppStoreServerNotifications/x5c.md)

## See Also

- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [transaction-data-types](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transaction-data-types.md)

---


## JWSRenewalInfoDecodedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object JWSRenewalInfoDecodedPayload
```

## Topics

### Data types

- [transaction-data-types](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transaction-data-types.md)

## See Also

- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)
- [JWSDecodedHeader](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSDecodedHeader.md)
- [transaction-data-types](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transaction-data-types.md)

---


## JWSTransaction

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string JWSTransaction
```

## 

The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransaction](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransaction) type is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the transaction information, signed by the App Store according to the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

- To read the transaction information, Base64URL-decode the payload. Use a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) object to read the payload information.
- To read the header, decode it and use a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader) object to access the information. Use the information in the header to verify the signature.

### 

To verify a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransaction](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransaction) on your server, consider implementing the verification using the App Store Server Library function `verifyAndDecodeTransaction`. The library provides this function in each language the library supports. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.documentation/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## See Also

- [JWSRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)

---


## JWSTransactionDecodedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object JWSTransactionDecodedPayload
```

## 

> **IMPORTANT:** Don’t use the `price` or `currency` values for any revenue reconciliation or recognition. App Store Connect reporting is your source of record for financial and accounting purposes. For more information, see [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

## Topics

### Data types

- [transaction-data-types](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transaction-data-types.md)

## See Also

- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [JWSDecodedHeader](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSDecodedHeader.md)
- [transaction-data-types](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transaction-data-types.md)

---


## advancedCommerceConsistencyToken

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceConsistencyToken
```

## See Also

- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommerceDescription

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceDescription
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommerceDescriptors

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceDescriptors
```

## See Also

- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedCommerceEstimatedTax

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 advancedCommerceEstimatedTax
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommerceOfferPrice

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 advancedCommerceOfferPrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommercePeriod

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommercePeriod
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommercePrice

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 advancedCommercePrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommercePriceIncreaseInfo

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommercePriceIncreaseInfo
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedCommercePriceIncreaseInfoDependentSKU

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommercePriceIncreaseInfoDependentSKU
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommercePriceIncreaseInfoPrice

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 advancedCommercePriceIncreaseInfoPrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommerceRefund

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceRefund
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedCommerceRefundAmount

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 advancedCommerceRefundAmount
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommerceRefundDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp advancedCommerceRefundDate
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedCommerceRefundType

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceRefundType
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedCommerceRenewalItem

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceRenewalItem
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedCommerceRequestReferenceId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceRequestReferenceId
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedCommerceSKU

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceSKU
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedCommerceTaxExclusivePrice

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 advancedCommerceTaxExclusivePrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedCommerceTaxRate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceTaxRate
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedCommerceTransactionInfo

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceTransactionInfo
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedCommerceTransactionItem

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceTransactionItem
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)

---


## advancedCommerceTransactionItems

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
[advancedCommerceTransactionItem] advancedCommerceTransactionItems
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedcommerce-datatypes

## 

For more information about [doc://com.apple.documentation/documentation/AdvancedCommerceAPI](doc://com.apple.documentation/documentation/AdvancedCommerceAPI), see [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/).

## Topics

### Data types

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)
- [advancedCommerceRefundType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundType.md)
- [advancedCommerceRefunds](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefunds.md)
- [advancedCommerceRenewalItems](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItems.md)
- [advancedCommerceRequestReferenceId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRequestReferenceId.md)
- [advancedCommerceSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceSKU.md)
- [advancedCommerceTaxCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTaxCode.md)
- [advancedCommerceTaxExclusivePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTaxExclusivePrice.md)
- [advancedCommerceTaxRate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTaxRate.md)
- [advancedCommerceTransactionItems](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItems.md)

### Objects

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedcommercedisplayname

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceDisplayName
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedcommerceoffer

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceOffer
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedcommerceofferperiod

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceOfferPeriod
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedcommerceperiodcount

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 advancedCommercePeriodCount
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedcommercepriceincreaseinfostatus

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommercePriceIncreaseInfoStatus
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedcommercereason

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceReason
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundReason.md)

---


## advancedcommercerefundreason

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceRefundReason
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedcommercerefunds

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
[advancedCommerceRefund] advancedCommerceRefunds
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedcommercerenewalinfo

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object advancedCommerceRenewalInfo
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefund.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceTransactionItem.md)

---


## advancedcommercerenewalitems

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
[advancedCommerceRenewalItem] advancedCommerceRenewalItems
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## advancedcommercetaxcode

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string advancedCommerceTaxCode
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedCommerceRefundDate.md)

---


## alg

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string alg
```

## See Also

- [x5c](../com.apple.appstoreservernotifications/AppStoreServerNotifications/x5c.md)

---


## app-store-server-notifications-changelog

## 

App Store Server Notifications has two versions of notifications. Version 1 notifications and the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint are deprecated. Instead, implement the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications.

To set up your server to receive notifications, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). Use this changelog to learn about feature updates, version information, deprecations, and removals for App Store Server Notifications.

### 

**New features**

- Added the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/revocationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/revocationType) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/revocationPercentage](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/revocationPercentage) fields to the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload).
- Added the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfo) object, and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoDependentSKU), [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoStatus), [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/advancedCommercePriceIncreaseInfoPrice), fields to the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload).

### 

**New features**

- Updated the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) to include the new payload object, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appData](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appData).
- Added the notification type `RESCIND_CONSENT` to [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType).

### 

**New features**

- Added the `ONE_TIME` value to [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerDiscountType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerDiscountType) to indicate In-App Purchase offer codes.

### 

**New features**

- Added the `ACTIVE_TOKEN_REMINDER` and `CREATED` values to [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype), which can appear in notifications with an `EXTERNAL_PURCHASE_TOKEN` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType).
- Updated [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken) to include the new fields [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/tokenType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/tokenType) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/tokenExpirationDate](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/tokenExpirationDate).

### 

**New features**

- The `ONE_TIME_CHARGE` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) is now available in the production environment.

### 

**New features**

- Added the notification types `METADATA_UPDATE` and `MIGRATE` to [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType).
- Added the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/previousOriginalTransactionId](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/previousOriginalTransactionId) field to the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload).

### 

**New features**

- Updated the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) to include the new [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appTransactionId](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appTransactionId) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerPeriod](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerPeriod) fields.
- Updated the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload) to include the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appAccountToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appAccountToken) field.

### 

**New features**

- Added support for the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI](doc://com.apple.documentation/documentation/AdvancedCommerceAPI).

### 

**New features**

- Updated the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload) to include the new field [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/eligibleWinBackOfferIds](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/eligibleWinBackOfferIds).
- Added the win-back offer type to [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerType).

### 

**New features**

- Added the notification type `ONE_TIME_CHARGE` to [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType). This notification type is currently available only in the sandbox environment.
- Added the fields [doc://com.apple.documentation/documentation/AppStoreServerAPI/renewalPrice](doc://com.apple.documentation/documentation/AppStoreServerAPI/renewalPrice), [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency), and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerDiscountType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerDiscountType) to the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload).

### 

**New features**

- Added the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/consumptionRequestReason](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/consumptionRequestReason) to the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data) object.
- The `CONSUMPTION_REQUEST` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) added notifications for refund requests for auto-renewable subscriptions.

### 

**New features**

- The type of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/price](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/price) field changed from `int32` to `int64`.

### 

**New features**

- Added a new [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType):  `EXTERNAL_PURCHASE_TOKEN` and a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype): `UNREPORTED`.
- Updated the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) to include the new payload object, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken).
- Added the types [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseId](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseId) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/tokenCreationDate](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/tokenCreationDate).

### 

**New features**

- Changed the notification type the App Store server sends when a customer redeems a subscription offer for an inactive subscription to the `SUBSCRIBED` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType). The App Store server only sends the `OFFER_REDEEMED` notification type when customers redeem an offer on an active subscription.

### 

**New features**

- Added new properties in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) object: [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/price](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/price), [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency), and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerDiscountType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerDiscountType).

### 

**New features**

- Added a new version 2 [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType), `REFUND_REVERSED`.
- Added the following new fields in the transaction decoded payload, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload): [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefront](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefront), [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefrontId](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefrontId), and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/transactionReason](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/transactionReason).
- Added the `renewalDate` field in the renewal info decoded payload, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload).
- Added a subscription [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/status](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/status) field in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data) object of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload).
- The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1) now includes a `deprecation` field.

**Deprecations**

- The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint and version 1 notifications are deprecated. Implement the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications instead.

### 

**New features**

- Added a new notification type for App Store Server Notifications 2 that consists of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) value `RENEWAL_EXTENSION` and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype) values of `SUMMARY` and `FAILURE`. This notification provides information when you extend the subscription renewal date for all active subscribers, based on a product identifier. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI).
- Updated the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) to include the new [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/summary](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/summary) object, which appears in the payload for a `RENEWAL_EXTENSION` notification with a `SUMMARY` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype).

### 

**New features**

- Added the `PRODUCT_NOT_FOR_SALE` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype) for the `EXPIRED` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType).

### 

**New features**

- App Store Server Notifications 2 supports sending a `TEST` notification. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType), and the endpoints [doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification) and [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Test-Notification-Status) in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI).

### 

**New features**

- In App Store Server Notifications 2, the notification subtype `ACCEPTED` is now sent when the App Store notifies the customer of an auto-renewable subscription price increase that doesn’t require customer consent. This notification subtype is available only in version 2 notifications. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype).

### 

**New features**

- [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) is available, and version 1 is still supported. For information about the notifications sent in version 2, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType), `substate`, and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2).
- For information about the notifications sent in version 1, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1) (previously named `responseBody`).

### 

**Deprecations**

- In [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/app-store-server-notifications-version-1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/app-store-server-notifications-version-1), the following notification type and top-level objects are deprecated and removed: `RENEWAL,latest_receipt`, `latest_receipt_info`, `latest_expired_receipt`, and `latest_expired_receipt_info`. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type).

### 

**New features**

- App Store Server Notifications is available.

## See Also

- [enabling-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/enabling-app-store-server-notifications.md)
- [receiving-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/receiving-app-store-server-notifications.md)
- [responding-to-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responding-to-app-store-server-notifications.md)

---


## app-store-server-notifications-v2

## 

To receive server notifications from the App Store, provide your secure server’s HTTPS URL in App Store Connect. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). To secure your server and receive notifications, your server must support the Transport Layer Security (TLS) protocol version 1.2 or later.

Upon receiving a server notification, respond to the App Store with an HTTP status code of `200-206` if the post was successful. If the post was unsuccessful, send HTTP `50x` or `40x` to have the App Store retry the notification. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

## See Also

- [responseBodyV2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2.md)
- [responseBodyV2DecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2DecodedPayload.md)
- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)

---


## app-store-server-notifications-version-1

## Topics

### Version 1 notifications

- [App-Store-Server-Notifications-V1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V1.md)
- [responseBodyV1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV1.md)
- [notification_type](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notification_type.md)

---


## appAccountToken

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
uuid appAccountToken
```

## 

When a customer initiates an in-app purchase, your app may create an [doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)](doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) and send it to the App Store. The App Store returns the same value in [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appAccountToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appAccountToken) in the transaction information after the customer completes the purchase.

If you’re using the [doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase) and provide a UUID in the [doc://com.apple.documentation/documentation/StoreKit/SKMutablePayment/applicationUsername](doc://com.apple.documentation/documentation/StoreKit/SKMutablePayment/applicationUsername) property, then the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appAccountToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appAccountToken) field contains that value.

---


## appData

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object appData
```

## 

The `appData` object is part of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). This object is present in the payload when the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) is `RESCIND_CONSENT`.

## Topics

### JWS app transaction information

- [JWSAppTransaction](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSAppTransaction.md)

## See Also

- [summary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/summary.md)
- [data](../com.apple.appstoreservernotifications/AppStoreServerNotifications/data.md)

---


## appappleid

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 appAppleId
```

## See Also

- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [bundleVersion](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleVersion.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [status](../com.apple.appstoreservernotifications/AppStoreServerNotifications/status.md)

---


## apptransactionid

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string appTransactionId
```

## 

For more information, see [doc://com.apple.documentation/documentation/StoreKit/AppTransaction/appTransactionID](doc://com.apple.documentation/documentation/StoreKit/AppTransaction/appTransactionID).

---


## autoRenewProductId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string autoRenewProductId
```

## See Also

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

---


## autorenewstatus

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 autoRenewStatus
```

## See Also

- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

---


## bundleId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string bundleId
```

## See Also

- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleVersion](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleVersion.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [status](../com.apple.appstoreservernotifications/AppStoreServerNotifications/status.md)

---


## bundleversion

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string bundleVersion
```

## See Also

- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [status](../com.apple.appstoreservernotifications/AppStoreServerNotifications/status.md)

---


## consumptionRequestReason

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string consumptionRequestReason
```

## 

When a customer initiates a refund request for a consumable in-app purchase or auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) to your server. The notification includes the `consumptionRequestReason` in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data) object.

---


## currency

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string currency
```

## 

The currency property contains an ISO 4217 alpha-3 string that represents the currency of the price of the product.

> **IMPORTANT:** For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency) value to infer the storefront. Use the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefront](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefront) value in the transaction instead.

For more information on how you set prices, see [https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) and [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [price](../com.apple.appstoreservernotifications/AppStoreServerNotifications/price.md)

---


## data

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object data
```

## 

The `data` object is part of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). It’s present in the payload for [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) values related to in-app purchases, except for the `RENEWAL_EXTENSION` notification type with a `SUMMARY` [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype), and the `EXTERNAL_PURCHASE_TOKEN` notification type.

Use the notification type along with the transaction and subscription renewal information in the `data` object to update a user’s service or present promotional offers according to your business logic.

## Topics

### App metadata and environment

- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [bundleVersion](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleVersion.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [status](../com.apple.appstoreservernotifications/AppStoreServerNotifications/status.md)

### JWS transaction and renewal info

- [JWSRenewalInfo](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)

### Consumption request info

- [consumptionRequestReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/consumptionRequestReason.md)

## See Also

- [summary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/summary.md)
- [appData](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appData.md)

---


## eligiblewinbackofferids

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
[offerIdentifier] eligibleWinBackOfferIds
```

## See Also

- [offerIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerPeriod.md)
- [offerType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerType.md)
- [offerDiscountType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerDiscountType.md)

---


## enabling-app-store-server-notifications

## 

[doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications) is a server-to-server service that sends real-time notifications for in-app purchase events, and notifications for unreported external purchase tokens. To enable notifications, set up an HTTPS URL on your server, and configure settings in App Store Connect.

For information about parsing and interpreting notifications, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/receiving-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/receiving-app-store-server-notifications).

### 

To receive server notifications from the App Store, your server must support the Transport Layer Security (TLS) 1.2 protocol or later.

To enable App Store Server Notifications, follow these steps:

1. Determine the HTTPS URL on your server to receive notifications for the production environment.
2. Optionally, determine the HTTPS URL on your server to receive notifications for the sandbox environment for testing notifications. You may use the same URL for both the production and the sandbox environments.
3. App Store Connect gives you the choice of receiving version 2 or version 1 notifications for each environment. To choose version 2, set up your endpoint as [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2).
4. Configure your URL in App Store Connect. For more information, see [https://help.apple.com/app-store-connect/#/dev0067a330b](https://help.apple.com/app-store-connect/#/dev0067a330b).

> **IMPORTANT:** If you specify a port in your URL, the port must be either `443` or greater than or equal to `1024`. For example, the URL `https://example.com:1234/notifications` specifies the port `1234`.

Configure your server to respond with HTTP status codes to indicate whether the App Store server notification `POST` is successful. For more information, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

For new implementations, use [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2). To transition from using version 1 notifications to version 2, test version 2 notifications in the sandbox environment before you update your production environment to version 2.

For information about changes to App Store Server Notifications, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).

### 

If your server requires IP addresses to be on an allow list, add the IP address subnet `17.0.0.0/8` to allow your server to receive notifications from the App Store server. This subnet applies to both the sandbox and the production environments.

### 

To determine whether your server is receiving notifications, call the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI). This endpoint asks the App Store server to send a notification with the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) `TEST`. Use the [doc://com.apple.documentation/documentation/AppStoreServerAPI/testNotificationToken](doc://com.apple.documentation/documentation/AppStoreServerAPI/testNotificationToken) you receive to call the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Test-Notification-Status) endpoint to learn how your server responds to the test notification.

The App Store server sends the `TEST` notification in the version 2 notification format. However, it sends it to your server regardless of whether you configure a version 1 or version 2 notification URL in App Store Connect.

## See Also

- [receiving-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/receiving-app-store-server-notifications.md)
- [responding-to-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responding-to-app-store-server-notifications.md)
- [app-store-server-notifications-changelog](../com.apple.appstoreservernotifications/AppStoreServerNotifications/app-store-server-notifications-changelog.md)

---


## environment

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string environment
```

## 

You receive notifications in the sandbox environment when you opt in to receive notifications in the sandbox environment and test your app in the sandbox environment. TestFlight also uses the sandbox environment to send notifications. To opt in to receive notifications, see [https://help.apple.com/app-store-connect/#/dev0067a330b](https://help.apple.com/app-store-connect/#/dev0067a330b). For more information about testing, see [doc://com.apple.documentation/documentation/StoreKit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox](doc://com.apple.documentation/documentation/StoreKit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox), and [https://developer.apple.com/testflight/](https://developer.apple.com/testflight/).

## See Also

- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [bundleVersion](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleVersion.md)
- [status](../com.apple.appstoreservernotifications/AppStoreServerNotifications/status.md)

---


## expirationIntent

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 expirationIntent
```

## See Also

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

---


## expiresdate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp expiresDate
```

## 

The `expiresDate` is a static value that applies for each transaction. When the auto-renewable subscription renews, the App Store creates a new transaction with a new `expiresDate`.

## See Also

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

---


## externalPurchaseId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string externalPurchaseId
```

## 

The `externalPurchaseId` is the field of an [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken) that uniquely identifies the token.

## See Also

- [tokenCreationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenCreationDate.md)
- [tokenExpirationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenExpirationDate.md)
- [tokenType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenType.md)

---


## externalPurchaseToken

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object externalPurchaseToken
```

## 

The `externalPurchaseToken` object is part of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). It’s present in the payload when the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) is `EXTERNAL_PURCHASE_TOKEN`. This notification type applies to apps that use the [doc://com.apple.documentation/documentation/StoreKit/external-purchase](doc://com.apple.documentation/documentation/StoreKit/external-purchase) API to offer alternative payment options.

The `externalPurchaseToken` object is the Base64URL-decoded JSON of the external purchase token your app or website receives when your customer initiates an external purchase. For more information on external purchase tokens, see [doc://com.apple.documentation/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens](doc://com.apple.documentation/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

To report tokens with or without associated transactions, call the [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint of the [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI) from your server.

## Topics

### External purchase token fields

- [externalPurchaseId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/externalPurchaseId.md)
- [tokenCreationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenCreationDate.md)
- [tokenExpirationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenExpirationDate.md)
- [tokenType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenType.md)

---


## failedCount

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 failedCount
```

## See Also

- [requestIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/requestIdentifier.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [storefrontCountryCodes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCodes.md)
- [storefrontCountryCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCode.md)
- [succeededCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/succeededCount.md)

---


## gracePeriodExpiresDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp gracePeriodExpiresDate
```

## 

For more information about billing grace periods, see [https://help.apple.com/app-store-connect/#/dev58bda3212](https://help.apple.com/app-store-connect/#/dev58bda3212).

## See Also

- [isInBillingRetryPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isInBillingRetryPeriod.md)

---


## inAppOwnershipType

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string inAppOwnershipType
```

---


## isUpgraded

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
boolean isUpgraded
```

## 

If `isUpgraded` is `true`, the customer has upgraded the subscription represented by this transaction to another subscription. This value appears in the transaction only when the value is `true`. To determine the service that the customer is entitled to, look for another transaction that has a subscription with a higher level of service. For more information about subscription groups and levels of service, see [https://developer.apple.com/app-store/subscriptions/](https://developer.apple.com/app-store/subscriptions/).

## See Also

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

---


## isinbillingretryperiod

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
boolean isInBillingRetryPeriod
```

## See Also

- [gracePeriodExpiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/gracePeriodExpiresDate.md)

---


## jwsapptransaction

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string JWSAppTransaction
```

## 

For more information, refer to [doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSAppTransaction](doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSAppTransaction).

---


## jwsrenewalinfo

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string JWSRenewalInfo
```

## 

The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfo](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfo) type is a string of three Base64 URL-encoded components, separated by a period. The string contains the JWS representation of the subscription renewal information, signed by the App Store according to the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components in the string are a header, a payload, and a signature, in that order.

To read the subscription renewal information, Base64 URL-decode the payload. Use a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload) object to read the payload information.

To read the header, Base64 URL-decode it and use a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader) object to access the information. Use the information in the header to verify the signature.

## See Also

- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)

---


## notificationType

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string notificationType
```

## 

The `notificationType appears` in the notification payload, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). It describes the event that leads to the notification. Some notifications also have a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype) that further describes the event. See the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) for more information about the notification in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data), [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/summary](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/summary), or [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken) object.

### 

When events occur that affect the customer’s In-App Purchase and subscription life cycle, the App Store server sends you notifications. The following tables list the notifications by life-cycle events.

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer purchases a consumable, non-consumable, or non-renewing subscription. | `ONE_TIME_CHARGE` |  |
| Customer redeems an offer code for a consumable, non-consumable, or non-renewing subscription. | `ONE_TIME_CHARGE` |  |
| Customer receives access to a non-consumable In-App Purchase through Family Sharing. | `ONE_TIME_CHARGE` |  |

Events that enable service for subscriptions, including initial subscriptions, resubscribing, and successful auto-renewals, result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer subscribes for the first time to any subscription within a subscription group. | `SUBSCRIBED` | `INITIAL_BUY` |
| Customer resubscribes to any subscription from the same subscription group as their expired subscription. | `SUBSCRIBED` | `RESUBSCRIBE` |
| The subscription successfully auto-renews. | `DID_RENEW` |  |
| A family member gains access to the subscription through Family Sharing after the purchaser subscribes for the first time. | `SUBSCRIBED` | `INITIAL_BUY` |
| A family member gains access to the subscription through Family Sharing after the purchaser resubscribes. | `SUBSCRIBED` | `RESUBSCRIBE` |

Customers changing their subscription options, including upgrading, downgrading, or canceling, result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer downgrades a subscription within the same subscription group. | `DID_CHANGE_RENEWAL_PREF` | `DOWNGRADE` |
| Customer reverts to the previous subscription, effectively canceling their downgrade. | `DID_CHANGE_RENEWAL_PREF` |  |
| Customer upgrades a subscription within the same subscription group. | `DID_CHANGE_RENEWAL_PREF` | `UPGRADE` |
| Customer cancels the subscription from the App Store Subscriptions settings page. | `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_DISABLED` |
| Customer subscribes again after canceling a subscription, which reenables auto-renew. | `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_ENABLED` |
| The system turned off auto-renew because the customer initiated a refund through your app using the refund request API. | `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_DISABLED` |

Customers redeeming offers, such as promotional offers, win-back offers, or offer codes result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Customer redeems a promotional offer or offer code for an active subscription. | `OFFER_REDEEMED` |  |
| Customer redeems an offer code to subscribe for the first time. | `SUBSCRIBED` | `INITIAL_BUY` |
| Customer redeems a promotional offer, offer code, or win-back offer after their subscription expired. | `SUBSCRIBED` | `RESUBSCRIBE` |
| Customer redeems a promotional offer or offer code to upgrade their subscription. | `OFFER_REDEEMED` | `UPGRADE` |
| Customer redeems a promotional offer and downgrades their subscription. | `OFFER_REDEEMED` | `DOWNGRADE` |
| Customer redeems an offer code for a consumable, non-consumable, or non-recurring subscription. | `ONE_TIME_CHARGE` |  |

Billing events, including billing retries, entering and exiting the billing grace period, and expiring subscriptions, result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| The subscription expires because the customer chose to cancel it. | `EXPIRED` | `VOLUNTARY` |
| The subscription expires because the developer removed the subscription from sale and the renewal fails. | `EXPIRED` | `PRODUCT_NOT_FOR_SALE` |
| The subscription expires because the billing retry period ends without recovering the subscription. | `EXPIRED` | `BILLING_RETRY` |
| The subscription fails to renew and enters the billing retry period. | `DID_FAIL_TO_RENEW` |  |
| The subscription fails to renew and enters the billing retry period with Billing Grace Period enabled. | `DID_FAIL_TO_RENEW` | `GRACE_PERIOD` |
| The billing retry successfully recovers the subscription. | `DID_RENEW` | `BILLING_RECOVERY` |
| The subscription exits the billing grace period (and continues in billing retry). | `GRACE_PERIOD_EXPIRED` |  |

Events or notifications that occur when you increase the price of an auto-renewable subscription include:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| The system informs the customer of the auto-renewable subscription price increase that requires customer consent, and the customer doesn’t respond. | `PRICE_INCREASE` | `PENDING` |
| The auto-renewable subscription expires because the customer didn’t consent to the price increase that requires consent. | `EXPIRED` | `PRICE_INCREASE` |
| Customer consents to an auto-renewable subscription price increase that requires consent. | `PRICE_INCREASE` | `ACCEPTED` |
| The system notifies the customer of the auto-renewable subscription price increase that doesn’t require customer consent. | `PRICE_INCREASE` | `ACCEPTED` |
| Customer canceled the subscription after receiving a price increase notice or a request to consent to a price increase. | `DID_CHANGE_RENEWAL_STATUS` |  |

Customers requesting refunds or canceling Family Sharing result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| Apple refunds the transaction for a consumable or non-consumable In-App Purchase, a non-renewing subscription, or an auto-renewable subscription. | `REFUND` |  |
| Apple reverses a previously granted refund due to a dispute that the customer raised. | `REFUND_REVERSED` |  |
| Apple declines a refund that the customer initiated in the app, using the request refund API. | `REFUND_DECLINED` |  |
| Apple requests consumption information for a refund request that a customer initiates. | `CONSUMPTION_REQUEST` |  |
| A family member loses access to the subscription through Family Sharing. | `REVOKE` |  |

Developers requesting subscription-renewal-date extensions result in the following notifications:

| Event | Notification type | Notification subtype |
| --- | --- | --- |
| The App Store successfully extends a subscription renewal date for a specific subscription. | `RENEWAL_EXTENDED` |  |
| The App Store successfully completes extending the subscription renewal date for all eligible subscribers. | `RENEWAL_EXTENSION` | `SUMMARY` |
| The App Store failed to extend the subscription renewal date for a specific subscriber. | `RENEWAL_EXTENSION` | `FAILURE` |

## See Also

- [App-Store-Server-Notifications-V2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V2.md)
- [responseBodyV2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2.md)
- [responseBodyV2DecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2DecodedPayload.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)

---


## notification_type

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string notification_type
```

## 

You receive and can react to server notifications in real time for the subscription and refund events that these notification type values describe. The `notification_type` appears in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1).

> **NOTE:** If you’re receiving App Store Server Notifications Version 2, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) instead.

### 

When events occur that affect the customer’s product and subscription life-cycle, your server receives notifications from the App Store. Here are some examples of product events and the server notifications you can expect to receive:

| Subscription or in-app purchase event | Notification types |
| --- | --- |
| Customer completed an initial purchase of a subscription | `INITIAL_BUY` |
| Subscription is active; customer upgraded to another SKU | `DID_CHANGE_RENEWAL_STATUS`, `INTERACTIVE_RENEWAL` |
| Subscription is active; customer downgraded to another SKU | `DID_CHANGE_RENEWAL_PREF` |
| Subscription has expired; customer resubscribed to the same SKU | `DID_CHANGE_RENEWAL_STATUS` |
| Subscription has expired; customer resubscribed to another SKU (upgrade or downgrade) | `INTERACTIVE_RENEWAL`, `DID_CHANGE_RENEWAL_STATUS` |
| Customer canceled the subscription from the App Store Subscriptions settings page. Their subscription will not auto-renew and will expire on the `expires_date` | `DID_CHANGE_RENEWAL_STATUS` |
| Customer previously canceled the subscription, but now resubscribed to same product before the subscription expired. The subscription will auto-renew on the `expires_date` | `DID_CHANGE_RENEWAL_STATUS` |
| AppleCare refunded a subscription | `CANCEL`, `DID_CHANGE_RENEWAL_STATUS` |
| Subscription failed to renew because of a billing issue | `DID_FAIL_TO_RENEW` |
| Expired subscription recovered by App Store through a billing retry | `DID_RECOVER` |
| Subscription churned after failed billing retry attempts | `DID_CHANGE_RENEWAL_STATUS` |
| AppleCare successfully refunded the transaction for a consumable, non-consumable, or a non-renewing subscription | `REFUND` |
| You’ve increased the price of an auto-renewable subscription and the price increase requires customer consent before the subscription auto-renews | `PRICE_INCREASE_CONSENT` |
| Subscription successfully auto-renewed | `DID_RENEW` |
| A purchaser disabled Family Sharing for a product, the purchaser (or family member) left the family group, or the purchaser asked for and received a refund | `REVOKE` |
| The customer initiated a refund request for a consumable in-app purchase | `CONSUMPTION_REQUEST` |

### 

The following table identifies the notifications you receive for the purchaser and for their family members who share products through Family Sharing. To determine if a notification is for the purchaser or a family member, check the value of the [doc://com.apple.documentation/documentation/AppStoreReceipts/in_app_ownership_type](doc://com.apple.documentation/documentation/AppStoreReceipts/in_app_ownership_type) field, which appears in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary) of the `responseBody` object. For more information about Family Sharing, see [doc://com.apple.documentation/documentation/StoreKit/supporting-family-sharing-in-your-app](doc://com.apple.documentation/documentation/StoreKit/supporting-family-sharing-in-your-app).

| Notification type | Received for Purchaser | Received for Family Members |
| --- | --- | --- |
| `CANCEL` | YES | NO |
| `CONSUMPTION_REQUEST` | YES | N/A |
| `DID_CHANGE_RENEWAL_PREF` | YES | YES |
| `DID_CHANGE_RENEWAL_STATUS` | YES | YES |
| `DID_FAIL_TO_RENEW` | YES | YES |
| `DID_RECOVER` | YES | YES |
| `DID_RENEW` | YES | YES |
| `INITIAL_BUY` | YES | NO |
| `INTERACTIVE_RENEWAL` | YES | YES |
| `PRICE_INCREASE_CONSENT` | YES | NO |
| `REFUND` | YES | NO |
| `REVOKE` | NO | YES |
| `RENEWAL` (Deprecated) | N/A | N/A |

The `CONSUMPTION_REQUEST` notification applies to consumable in-app purchases, which aren’t eligible for Family Sharing.

### 

Your development-signed apps use the sandbox environment when you sign in to App Store using a Sandbox Apple Account. To create a Sandbox Apple Account or test account in App Store Connect, see [https://help.apple.com/app-store-connect/#/dev8b997bee1](https://help.apple.com/app-store-connect/#/dev8b997bee1).

If you enabled App Store Server Notifications, test your logic for transactions in the sandbox environment. To determine if a notification for a subscription event occurred in the test environment, check whether the value of the `environment` field in the JSON [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1) object equals `Sandbox`.

The following notification types are available in sandbox: `INITIAL_BUY`, `DID_CHANGE_RENEWAL_PREF`, `DID_CHANGE_RENEWAL_STATUS`, `DID_RENEW`, `INTERACTIVE_RENEWAL`, `CANCEL`, and `REFUND`. Notifications in the sandbox environment are for the purchaser only, and have [doc://com.apple.documentation/documentation/AppStoreReceipts/in_app_ownership_type](doc://com.apple.documentation/documentation/AppStoreReceipts/in_app_ownership_type) equal to `PURCHASED`. For more information about testing in-app purchases, see [doc://com.apple.documentation/documentation/StoreKit/testing-in-app-purchases-with-sandbox](doc://com.apple.documentation/documentation/StoreKit/testing-in-app-purchases-with-sandbox).

## See Also

- [App-Store-Server-Notifications-V1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V1.md)
- [responseBodyV1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV1.md)

---


## notificationuuid

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string notificationUUID
```

## 

The App Store server assigns a unique identifer to each notification it sends. Use this value to identify, and ignore, duplicate notifications.

## See Also

- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)
- [version](../com.apple.appstoreservernotifications/AppStoreServerNotifications/version.md)
- [signedDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/signedDate.md)

---


## offerType

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 offerType
```

## 

All offer types, except offer type `1`, have an [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerIdentifier](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerIdentifier).

You set up offers in App Store Connect. For more information on subscription offers, see [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions), [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes), and [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers). For more information on offer codes, see [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases).

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreservernotifications/AppStoreServerNotifications/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerPeriod.md)
- [offerDiscountType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerDiscountType.md)

---


## offerdiscounttype

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string offerDiscountType
```

## 

Offer discount types apply to auto-renewable subscriptions except for `ONE_TIME`, which applies to the consumable, non-consumable, and non-renewing subscription product types.

You set up offers and determine the payment mode when you configure subscriptions and offers in App Store Connect. For more information about the Free Trial, Pay As You Go, and Pay Up Front payment modes, see [https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability](https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

For more information on configuring offers, see: [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions), [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes), and [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases).

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreservernotifications/AppStoreServerNotifications/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerPeriod.md)
- [offerType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerType.md)

---


## offeridentifier

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string offerIdentifier
```

## 

The `offerIdentifier` is a string that you provide in App Store Connect when you set up an offer. All offer types ([doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerType)) have offer identifiers, except for introductory offers.

For more information on offer codes, see [doc://com.apple.documentation/documentation/StoreKit/supporting-offer-codes-in-your-app](doc://com.apple.documentation/documentation/StoreKit/supporting-offer-codes-in-your-app). For more information on promotional offers, see [https://help.apple.com/app-store-connect/#/dev16dfca448](https://help.apple.com/app-store-connect/#/dev16dfca448).

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreservernotifications/AppStoreServerNotifications/eligibleWinBackOfferIds.md)
- [offerPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerPeriod.md)
- [offerType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerType.md)
- [offerDiscountType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerDiscountType.md)

---


## offerperiod

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string offerPeriod
```

## 

This field is in ISO 8601 duration format.

The following table shows examples of offer period values.

| Single period length | Period count | Offer period value |
| --- | --- | --- |
| 1 month | 1 | `P1M` |
| 1 month | 2 | `P2M` |
| 3 days | 1 | `P3D` |

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreservernotifications/AppStoreServerNotifications/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerIdentifier.md)
- [offerType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerType.md)
- [offerDiscountType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerDiscountType.md)

---


## originalPurchaseDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp originalPurchaseDate
```

## 

The original purchase date is in UNIX time, in milliseconds.

## See Also

- [purchaseDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/purchaseDate.md)
- [recentSubscriptionStartDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/recentSubscriptionStartDate.md)

---


## originalTransactionId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string originalTransactionId
```

## 

This value is identical to the transaction identifier ([doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/transactionId](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/transactionId)) except when the user restores or renews a subscription.

## See Also

- [transactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transactionId.md)
- [webOrderLineItemId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/webOrderLineItemId.md)
- [previousOriginalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/previousOriginalTransactionId.md)

---


## previousOriginalTransactionId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string previousOriginalTransactionId
```

## See Also

- [originalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalTransactionId.md)
- [transactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transactionId.md)
- [webOrderLineItemId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/webOrderLineItemId.md)

---


## price

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 price
```

## 

This value represents the price, in milliunits of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency), of the In-App Purchase that the system records in the transaction. One unit of the currency equals 1000 milliunits.

The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/price](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/price) value reflects all of the following:

- The price you configured in App Store Connect, which the system records on the purchase date ([doc://com.apple.documentation/documentation/AppStoreServerAPI/purchaseDate](doc://com.apple.documentation/documentation/AppStoreServerAPI/purchaseDate)).
- The discount from an offer in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerIdentifier](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerIdentifier) field, if the transaction includes an offer.
- The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/quantity](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/quantity) of a consumable In-App Purchase. The price value shows the total amount of the transaction for the quantity the customer purchased.

The following table shows some examples of the [doc://com.apple.documentation/documentation/AppStoreServerAPI/price](doc://com.apple.documentation/documentation/AppStoreServerAPI/price) and [doc://com.apple.documentation/documentation/AppStoreServerAPI/currency](doc://com.apple.documentation/documentation/AppStoreServerAPI/currency) parameters based on sample prices you might configure in App Store Connect:

| Configured price in App Store Connect | `price` parameter | `currency` parameter |
| --- | --- | --- |
| $1.99 (U.S. dollar) | 1990 | USD |
| KRW 3300 (South Korean won) | 3300000 | KRW |
| JPY 300 (Japanese yen) | 300000 | JPY |

To determine the storefront, use the [doc://com.apple.documentation/documentation/AppStoreServerAPI/storefront](doc://com.apple.documentation/documentation/AppStoreServerAPI/storefront) value in the transaction. Don’t use the [doc://com.apple.documentation/documentation/AppStoreServerAPI/currency](doc://com.apple.documentation/documentation/AppStoreServerAPI/currency) value to infer the storefront.

> **IMPORTANT:** For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

For more information on how you set prices, see [https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) and [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [currency](../com.apple.appstoreservernotifications/AppStoreServerNotifications/currency.md)

---


## priceincreasestatus

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 priceIncreaseStatus
```

## 

For more information about managing prices, see [https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers](https://developer.apple.com/app-store/subscriptions/#managing-prices-for-existing-subscribers) and [https://help.apple.com/app-store-connect/#/devc9870599e](https://help.apple.com/app-store-connect/#/devc9870599e).

---


## productId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string productId
```

## 

You create product identifiers for in-app purchases in App Store Connect.

## See Also

- [requestIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/requestIdentifier.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [storefrontCountryCodes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCodes.md)
- [storefrontCountryCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCode.md)
- [failedCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/failedCount.md)
- [succeededCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/succeededCount.md)

---


## purchaseDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp purchaseDate
```

## 

The purchase date is in UNIX time, in milliseconds.

## See Also

- [originalPurchaseDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalPurchaseDate.md)
- [recentSubscriptionStartDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/recentSubscriptionStartDate.md)

---


## quantity

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 quantity
```

## See Also

- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [type](../com.apple.appstoreservernotifications/AppStoreServerNotifications/type.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subscriptionGroupIdentifier.md)

---


## receiving-app-store-server-notifications

## 

The App Store delivers JSON objects using an HTTP POST to your server for notable in-app purchase events and unreported external purchase tokens. Your server is responsible for parsing, interpreting, and responding to all server-to-server notification posts. For more information about responding, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

The body of the POST contains the data elements described in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2) for version 2 notifications, and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1) for version 1. Parse them using the following information:

- The version 2 response body, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2), contains a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/signedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/signedPayload) that’s cryptographically signed by the App Store in JSON Web Signature (JWS) format. The JWS format increases security and enables you to decode and validate the signature on your server.  Some notifications include a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data) object, which has transaction and subscription renewal information that the App Store signs in JWS. The [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI) and the StoreKit [doc://com.apple.documentation/documentation/StoreKit/in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/in-app-purchase) API use the same JWS-signed format for transaction and subscription status information. For more information about JWS, see the [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.
- The version 1 response body, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1), is a JSON object. It includes the receipt that contains the most recent in-app purchase transaction for the app. For more information, see the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/unified_receipt](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/unified_receipt) object.

> **IMPORTANT:** The [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint and version 1 notifications, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notification_type), are deprecated. Instead, implement the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications.

Use the notification type along with the transaction and subscription renewal information to update a user’s service or present promotional offers according to your business logic. For information on handling notifications that contain an external purchase token, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken).

## See Also

- [enabling-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/enabling-app-store-server-notifications.md)
- [responding-to-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responding-to-app-store-server-notifications.md)
- [app-store-server-notifications-changelog](../com.apple.appstoreservernotifications/AppStoreServerNotifications/app-store-server-notifications-changelog.md)

---


## recentsubscriptionstartdate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp recentSubscriptionStartDate
```

## 

For more information about the recent subscription start date, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerAPI/recentSubscriptionStartDate).

> **IMPORTANT:** Don’t use the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) date to calculate days of paid service. For more information about paid days of service, see [https://developer.apple.com/app-store/subscriptions/#revenue-after-one-year](https://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

## See Also

- [originalPurchaseDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalPurchaseDate.md)
- [purchaseDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/purchaseDate.md)

---


## renewalDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp renewalDate
```

## 

The `renewalDate` is a value that’s always present in the payload for auto-renewable subscriptions, even for expired subscriptions. This date indicates the expiration date of the most recent auto-renewable subscription purchase, including renewals, and may be in the past. For subscriptions that renew successfully, the `renewalDate` is the date when the subscription renews.

## See Also

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

---


## renewalPrice

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 renewalPrice
```

## 

This value represents the renewal price, in milliunits of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency), of the auto-renewable subscription. One unit of the currency equals 1000 milliunits.

If the next billing period includes an offer specified by the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerIdentifier](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/offerIdentifier), the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/renewalPrice](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/renewalPrice) value reflects the discount.

> **IMPORTANT:** For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

To determine the storefront, use the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefront](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/storefront) value in the transaction. Don’t use the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/currency) value to infer the storefront.

## See Also

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)

---


## requestidentifier

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
uuid requestIdentifier
```

## 

You originally specify the `requestIdentifier` when you call [doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI).

## See Also

- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [storefrontCountryCodes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCodes.md)
- [storefrontCountryCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCode.md)
- [failedCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/failedCount.md)
- [succeededCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/succeededCount.md)

---


## responding-to-app-store-server-notifications

## 

When you set up the endpoints on your server to receive notifications, configure your server to send a response. Use HTTP status codes to indicate whether the App Store server notification post succeeded:

- Send HTTP `200`, or any HTTP code between `200` and `206`, if the post was successful.
- Send HTTP `50x` or `40x` to have the App Store retry the notification, if the post didn’t succeed.

The system considers all other HTTP codes an unsuccessful post. Your server isn’t required to return a data value.

If the App Store server doesn’t receive a success response from your server after the initial notification attempt, it retries as follows:

- For version 2 notifications, it retries five times, at 1, 12, 24, 48, and 72 hours after the previous attempt.
- For version 1 notifications, it retries three times, at 6, 24, and 48 hours after the previous attempt.

> **NOTE:** Retry notifications are available only in the production environment. In the sandbox environment, the App Store server attempts to send the notification one time.

### 

If your server misses notifications due to an outage, you can always get up-to-date transaction information by calling [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI) endpoints including [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Transaction-History) and [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses).

If you use version 2 notifications ([doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2)), you can recover missed notifications by calling [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Notification-History). You can also test whether your server is receiving and responding to version 2 notifications correctly by calling the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.documentation/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint.

## See Also

- [enabling-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/enabling-app-store-server-notifications.md)
- [receiving-app-store-server-notifications](../com.apple.appstoreservernotifications/AppStoreServerNotifications/receiving-app-store-server-notifications.md)
- [app-store-server-notifications-changelog](../com.apple.appstoreservernotifications/AppStoreServerNotifications/app-store-server-notifications-changelog.md)

---


## responseBodyV1

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object responseBodyV1
```

## 

Use the information in the response body to react quickly to changes in your users’ subscription states. The fields available in a notification sent to your server depend on the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1/notification_type](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV1/notification_type), which indicates the event that triggered the notification.

## Topics

### Unified receipt object

- [unified_receipt](../com.apple.appstoreservernotifications/AppStoreServerNotifications/unified_receipt.md)

## See Also

- [App-Store-Server-Notifications-V1](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V1.md)
- [notification_type](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notification_type.md)

---


## responseBodyV2

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object responseBodyV2
```

## 

The `signedPayload` object is a JWS representation. To get the transaction and subscription renewal details from the notification payload, process the `signedPayload` as follows:

1. Parse `signedPayload` to identify the JWS header, payload, and signature representations.
2. Base64URL-decode the payload to get the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). The decoded payload contains details of the notification such as the notification type and  data.
3. The `data` object contains a `signedTransactionInfo` ([doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSTransaction](doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSTransaction)) and based on the notification type, a `signedRenewalInfo` ([doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfo](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSRenewalInfo)). Parse and Base64URL-decode these signed JWS representations to get transaction and subscription renewal details.

Each of the signed JWS representations, `signedPayload`, `signedTransactionInfo`, and `signedRenewalInfo`, have a JWS signature that you can validate on your server. Use the algorithm specified in the header’s [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/alg](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/alg) parameter to validate the signature. For more information about validating signatures, see the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

## Topics

### Response body payload

- [signedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/signedPayload.md)

## See Also

- [App-Store-Server-Notifications-V2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V2.md)
- [responseBodyV2DecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2DecodedPayload.md)
- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)

---


## responseBodyV2DecodedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object responseBodyV2DecodedPayload
```

## 

The `responseBodyV2DecodedPayload` is the Base64URL-decoded notification information from the JWS payload portion of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/signedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/signedPayload). Use the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) and [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype) to understand the event that led to this notification.

The payload can contain only one of the following four fields:

- A [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/data) object, which contains details including the environment, the app metadata, and the signed transaction and subscription renewal information.
- An [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appData](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/appData) object, which contains details including the environment, the app metadata, and the signed app transaction information.
- A [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/summary](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/summary) object, which contains information only when the notification is a `RENEWAL_EXTENSION` with a `SUMMARY` subtype. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers).
- An [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken) object, which contains an external purchase token only when the notification is `EXTERNAL_PURCHASE_TOKEN`. For more information about this notification, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken).

## Topics

### Response objects for in-app purchases

- [summary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/summary.md)
- [data](../com.apple.appstoreservernotifications/AppStoreServerNotifications/data.md)
- [appData](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appData.md)

### Response object for an external purchase

- [externalPurchaseToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/externalPurchaseToken.md)

### Response types

- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)
- [version](../com.apple.appstoreservernotifications/AppStoreServerNotifications/version.md)
- [signedDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/signedDate.md)
- [notificationUUID](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationUUID.md)

### JWS header and payload data types

- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [JWSDecodedHeader](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSDecodedHeader.md)
- [transaction-data-types](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transaction-data-types.md)

## See Also

- [App-Store-Server-Notifications-V2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V2.md)
- [responseBodyV2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2.md)
- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)

---


## revocationDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp revocationDate
```

## See Also

- [revocationPercentage](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationPercentage.md)
- [revocationReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationReason.md)
- [revocationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationType.md)

---


## revocationType

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string revocationType
```

## 

If the `revocationType` is `REFUND_PRORATED`, see the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/revocationPercentage](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/revocationPercentage) for the prorated percentage.

## See Also

- [revocationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationDate.md)
- [revocationPercentage](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationPercentage.md)
- [revocationReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationReason.md)

---


## revocationpercentage

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 revocationPercentage
```

## 

The revocation percentage value is rounded to three decimal places of precision, and is expressed as an integer, in milliunits. This field is present in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) for  refunded transactions. This field doesn’t appear if the refund is reversed.

The following table shows several examples of revocation percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
| --- | --- |
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

## See Also

- [revocationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationDate.md)
- [revocationReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationReason.md)
- [revocationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationType.md)

---


## revocationreason

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 revocationReason
```

## 

For Family Sharing transactions, the revocation reason value is `0` if the customer leaves the family group or the owner stops sharing. If the purchaser of a Family Sharing transaction receives a refund, the revocation reason for Family Sharing transactions matches the value of the purchaser’s revocation reason.

## See Also

- [revocationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationDate.md)
- [revocationPercentage](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationPercentage.md)
- [revocationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationType.md)

---


## signedDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp signedDate
```

## 

This timestamp indicates the time the system signs the data before it sends the notification to your server. The notification payload contains a snapshot of the state of the transaction at this time.

This timestamp remains the same if the system resends the notification during a retry. For more information about retries, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

If you process multiple notifications for the same transaction ID, use the notification with the most recent `signedDate`, because it contains the most recent snapshot of the transaction’s status.

## See Also

- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)
- [version](../com.apple.appstoreservernotifications/AppStoreServerNotifications/version.md)
- [notificationUUID](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationUUID.md)

---


## signedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string signedPayload
```

## 

The `signedPayload` is a string of three Base64URL-encoded components, separated by a period. The string contains a JWS representation of the notification response body, signed by the App Store according to the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

To read the notification response body, Base64URL-decode the payload. Use a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) object to read the payload information.

To read the header, Base64URL-decode it and use a [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/JWSDecodedHeader) object to access the information. Use the information in the decoded header to verify the signature.

---


## status

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int32 status
```

## 

This status value is current as of the `signedDate` in the decoded payload, [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload).

## See Also

- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [bundleVersion](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleVersion.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)

---


## storefront

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string storefront
```

## 

This property uses the ISO 3166-1 alpha-3 country code representation. This property is the same as the [doc://com.apple.documentation/documentation/StoreKit/Storefront/countryCode](doc://com.apple.documentation/documentation/StoreKit/Storefront/countryCode) in StoreKit.

## See Also

- [storefrontId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontId.md)

---


## storefrontId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string storefrontId
```

## 

This value is the same as the [doc://com.apple.documentation/documentation/StoreKit/Storefront/id](doc://com.apple.documentation/documentation/StoreKit/Storefront/id) value in StoreKit.

## See Also

- [storefront](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefront.md)

---


## storefrontcountrycode

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string storefrontCountryCode
```

## 

This type uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

- [requestIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/requestIdentifier.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [storefrontCountryCodes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCodes.md)
- [failedCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/failedCount.md)
- [succeededCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/succeededCount.md)

---


## storefrontcountrycodes

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
[storefrontCountryCode] storefrontCountryCodes
```

## 

If you provide a list of storefronts when you call the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint, the notification returns only those storefronts. If you don’t use the `storefrontCountryCodes`, the subscription-renewal-date extension applies to all storefronts.

For information about providing the list of storefronts, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.documentation/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest).

## See Also

- [requestIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/requestIdentifier.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [storefrontCountryCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCode.md)
- [failedCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/failedCount.md)
- [succeededCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/succeededCount.md)

---


## subscriptionGroupIdentifier

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string subscriptionGroupIdentifier
```

## 

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [https://help.apple.com/app-store-connect/#/dev75708c031](https://help.apple.com/app-store-connect/#/dev75708c031).

## See Also

- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [type](../com.apple.appstoreservernotifications/AppStoreServerNotifications/type.md)
- [quantity](../com.apple.appstoreservernotifications/AppStoreServerNotifications/quantity.md)

---


## subtype

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string subtype
```

## 

This `subtype` field is part of the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload), and further describes an event of type [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType). It’s present only for specific version 2 notifications.

## See Also

- [App-Store-Server-Notifications-V2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/App-Store-Server-Notifications-V2.md)
- [responseBodyV2](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2.md)
- [responseBodyV2DecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/responseBodyV2DecodedPayload.md)
- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)

---


## succeededcount

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
int64 succeededCount
```

## See Also

- [requestIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/requestIdentifier.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [storefrontCountryCodes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCodes.md)
- [storefrontCountryCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCode.md)
- [failedCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/failedCount.md)

---


## summary

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object summary
```

## 

The `summary` object appears in the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) when the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/notificationType) is `RENEWAL_EXTENSION` and the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/subtype) is `SUMMARY`. This notification occurs when the App Store completes your request to extend the subscription renewal date for eligible subscribers. For more information about this request, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.documentation/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) in the [doc://com.apple.documentation/documentation/AppStoreServerAPI](doc://com.apple.documentation/documentation/AppStoreServerAPI).

## Topics

### Data types

- [requestIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/requestIdentifier.md)
- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)
- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)
- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [storefrontCountryCodes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCodes.md)
- [storefrontCountryCode](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontCountryCode.md)
- [failedCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/failedCount.md)
- [succeededCount](../com.apple.appstoreservernotifications/AppStoreServerNotifications/succeededCount.md)

## See Also

- [data](../com.apple.appstoreservernotifications/AppStoreServerNotifications/data.md)
- [appData](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appData.md)

---


## tokenExpirationDate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp tokenExpirationDate
```

## See Also

- [externalPurchaseId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/externalPurchaseId.md)
- [tokenCreationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenCreationDate.md)
- [tokenType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenType.md)

---


## tokenType

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string tokenType
```

### 

The token type field is present only for custom link tokens. For more information on tokens, see [doc://com.apple.documentation/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens](doc://com.apple.documentation/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

## See Also

- [externalPurchaseId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/externalPurchaseId.md)
- [tokenCreationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenCreationDate.md)
- [tokenExpirationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenExpirationDate.md)

---


## tokencreationdate

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
timestamp tokenCreationDate
```

## 

This field represents the date when the system created the [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/externalPurchaseToken).

## See Also

- [externalPurchaseId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/externalPurchaseId.md)
- [tokenExpirationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenExpirationDate.md)
- [tokenType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/tokenType.md)

---


## transaction-data-types

## Topics

### Environment

- [environment](../com.apple.appstoreservernotifications/AppStoreServerNotifications/environment.md)

### Transaction identifiers

- [originalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalTransactionId.md)
- [transactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transactionId.md)
- [webOrderLineItemId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/webOrderLineItemId.md)
- [previousOriginalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/previousOriginalTransactionId.md)

### App transaction identifier

- [appTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appTransactionId.md)

### App information

- [appAppleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAppleId.md)
- [bundleId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/bundleId.md)

### Account information

- [appAccountToken](../com.apple.appstoreservernotifications/AppStoreServerNotifications/appAccountToken.md)

### Product information

- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [type](../com.apple.appstoreservernotifications/AppStoreServerNotifications/type.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subscriptionGroupIdentifier.md)
- [quantity](../com.apple.appstoreservernotifications/AppStoreServerNotifications/quantity.md)

### Product price and currency

- [price](../com.apple.appstoreservernotifications/AppStoreServerNotifications/price.md)
- [currency](../com.apple.appstoreservernotifications/AppStoreServerNotifications/currency.md)

### Storefront information

- [storefront](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefront.md)
- [storefrontId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/storefrontId.md)

### Offers

- [eligibleWinBackOfferIds](../com.apple.appstoreservernotifications/AppStoreServerNotifications/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerPeriod.md)
- [offerType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerType.md)
- [offerDiscountType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/offerDiscountType.md)

### Purchase dates

- [originalPurchaseDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalPurchaseDate.md)
- [purchaseDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/purchaseDate.md)
- [recentSubscriptionStartDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/recentSubscriptionStartDate.md)

### Billing status

- [isInBillingRetryPeriod](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isInBillingRetryPeriod.md)
- [gracePeriodExpiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/gracePeriodExpiresDate.md)

### Subscripton renewal and expiration

- [autoRenewStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expirationIntent.md)
- [expiresDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/expiresDate.md)
- [isUpgraded](../com.apple.appstoreservernotifications/AppStoreServerNotifications/isUpgraded.md)
- [renewalDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalDate.md)
- [renewalPrice](../com.apple.appstoreservernotifications/AppStoreServerNotifications/renewalPrice.md)

### Family Sharing

- [inAppOwnershipType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/inAppOwnershipType.md)

### Price increase status

- [priceIncreaseStatus](../com.apple.appstoreservernotifications/AppStoreServerNotifications/priceIncreaseStatus.md)

### Revocations

- [revocationDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationDate.md)
- [revocationPercentage](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationPercentage.md)
- [revocationReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationReason.md)
- [revocationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/revocationType.md)

### Transaction reason

- [transactionReason](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transactionReason.md)

### JWS signature date

- [signedDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/signedDate.md)

### Advanced Commerce API data

- [advancedcommerce-datatypes](../com.apple.appstoreservernotifications/AppStoreServerNotifications/advancedcommerce-datatypes.md)

## See Also

- [JWSTransactionDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSRenewalInfoDecodedPayload.md)
- [JWSDecodedHeader](../com.apple.appstoreservernotifications/AppStoreServerNotifications/JWSDecodedHeader.md)

---


## transactionId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string transactionId
```

## 

The App Store generates a new value for transaction identifier every time the subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always matches the original transaction identifier ([doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/originalTransactionId](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/originalTransactionId)). For a restore or renewal, the transaction identifier doesn’t match the original transaction identifier. If a user restores or renews the same subscription multiple times, each restore or renewal has a unique transaction identifier.

## See Also

- [originalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalTransactionId.md)
- [webOrderLineItemId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/webOrderLineItemId.md)
- [previousOriginalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/previousOriginalTransactionId.md)

---


## transactionreason

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string transactionReason
```

## 

If a customer upgrades an auto-renewable subscription, the upgrade is effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change occurs on the subscription renewal date. The resulting `transactionReason` is `RENEWAL`.

---


## type

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string type
```

## See Also

- [productId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/productId.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subscriptionGroupIdentifier.md)
- [quantity](../com.apple.appstoreservernotifications/AppStoreServerNotifications/quantity.md)

---


## unified_receipt

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
object unified_receipt
```

## Topics

### Objects

- [Latest_receipt_info-data.dictionary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary.md)
- [Pending_renewal_info-data.dictionary](../com.apple.appstoreservernotifications/AppStoreServerNotifications/unified_receipt/Pending_renewal_info-data.dictionary.md)

---


## version

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string version
```

## 

The version string is `“2.0”`. It’s present in [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload) for version 2 notifications.

For more information about App Store Server Notification changes, see [doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog](doc://com.apple.appstoreservernotifications/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).

## See Also

- [notificationType](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationType.md)
- [subtype](../com.apple.appstoreservernotifications/AppStoreServerNotifications/subtype.md)
- [signedDate](../com.apple.appstoreservernotifications/AppStoreServerNotifications/signedDate.md)
- [notificationUUID](../com.apple.appstoreservernotifications/AppStoreServerNotifications/notificationUUID.md)

---


## webOrderLineItemId

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
string webOrderLineItemId
```

## 

This value applies only to auto-renewable subscriptions.

## See Also

- [originalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/originalTransactionId.md)
- [transactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/transactionId.md)
- [previousOriginalTransactionId](../com.apple.appstoreservernotifications/AppStoreServerNotifications/previousOriginalTransactionId.md)

---


## x5c

## Declaration

**Platforms:** Unsupported OS: App Store Server Notifications

```swift
[string] x5c
```

## 

For more information, or to download Apple’s root and intermediate certificates, see [https://www.apple.com/certificateauthority/](https://www.apple.com/certificateauthority/).

## See Also

- [alg](../com.apple.appstoreservernotifications/AppStoreServerNotifications/alg.md)

---

