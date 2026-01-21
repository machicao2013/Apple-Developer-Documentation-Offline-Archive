# appstoreserverapi

*Merged documentation for appstoreserverapi*

---

# App Store Server API

## 

The App Store Server API is a REST API that you call from your server to request and provide information about your customers’ In-App Purchases. The App Store signs the transaction and subscription renewal information that this API returns using the [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification. Most endpoints return data for a single customer of your app, indicated by a transaction identifier that you provide.

The App Store Server API is independent of the app’s installation status on the customers’ devices. The App Store server returns information based on a customer’s In-App Purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

This API provides the following functionality:

- **Transactions and auto-renewable subscription status.** Get information for single transactions by calling [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info) or a customer’s entire transaction history using [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History). Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses) for up-to-date subscription status. Use this information to keep your customers’ purchase information current on your server.
- **Refund information.** Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History) to get a customer’s refund history. Use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) endpoint to send information to the App Store when customers request a refund for an In-App Purchase, after you receive the `CONSUMPTION_REQUEST` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) from [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2). Your data helps inform refund decisions.
- **App Store Server Notifications history and testing.** Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) to request the notifications your server may have missed in the past 180 days (or 30 days in the sandbox environment). Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status) to test if your server is successfully receiving notifications at its [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint.
- **Subscription renewal date extensions.** Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) and related endpoints to compensate your customers for temporary service outages, canceled events, or interruptions to live-streamed events by extending the renewal date of their paid, active subscription. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).
- **Order information lookup.** Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID) to get In-App Purchase information based on a customer’s order ID, found on the App Store receipt that customers receive in email.
- **App transaction information and setting an app account token.** Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info) to get details about the customer’s purchase of your app, such as the original purchase date and version. Use [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token) to set an app account token when your customer makes an In-App Purchase outside your app, or to update its value.

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to use the App Store Server API.

Check the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/app-store-server-api-changelog](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/app-store-server-api-changelog) to learn about the latest changes to this API. Look for videos about the App Store Server API on the [https://developer.apple.com/videos/all-videos/?q=%22App%20Store%20Server%20API%22](https://developer.apple.com/videos/all-videos/?q=%22App%20Store%20Server%20API%22).

### 

Calls to the API require JSON Web Tokens (JWTs) for authorization; you obtain keys to create the tokens from your organization’s App Store Connect account. See [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests) to create your keys. See [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests) to generate tokens using your keys, and send API requests.

After you have a complete and signed token, provide the token in the request’s authorization header as a bearer token. Generate a new token for each new API request, or reuse tokens until they expire.

### 

The App Store Server Library is an open source library from Apple, available in four languages. It provides a client that make it easier to adopt the App Store Server APIs, including creating the JWTs to authorize calls. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library) and the WWDC23 session [https://developer.apple.com/videos/play/wwdc2023/10143/](https://developer.apple.com/videos/play/wwdc2023/10143/).

### 

All App Store Server API endpoints are available for testing in the sandbox environment, except [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID). Access the sandbox environment by sending requests to the endpoints using the following base URL:

```other
https://api.storekit-sandbox.itunes.apple.com/
```

For example, to call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) in the sandbox environment, send a request using the sandbox URL:

```other
https://api.storekit-sandbox.itunes.apple.com/inApps/v2/history/{transactionId}
```

Note that `/inApps` in the path is case-sensitive.

For endpoints that take a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId) as a parameter, be sure to call the endpoint using the same environment that creates the transaction identifier. Environment information is present in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/environment](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/environment) property of the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload).

If you don’t have environment information, follow these steps:

1. Call the endpoint using the production URL. If the call succeeds, the transaction identifier belongs to the production environment.
2. If you receive an error code `4040010` [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionIdNotFoundError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionIdNotFoundError), call the endpoint using the sandbox environment.
3. If the call succeeds, the transaction identifier belongs to the sandbox environment. If the call fails with the `4040010` error code, the transaction identifier isn’t present in either environment.

## Topics

### Essentials

- [simplifying-your-implementation-by-using-the-app-store-server-library](../com.apple.appstoreserverapi/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library.md)
- [creating-api-keys-to-authorize-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
- [generating-json-web-tokens-for-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
- [identifying-rate-limits](../com.apple.appstoreserverapi/AppStoreServerAPI/identifying-rate-limits.md)
- [app-store-server-api-changelog](../com.apple.appstoreserverapi/AppStoreServerAPI/app-store-server-api-changelog.md)

### In-App Purchase history

- [Get-Transaction-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History.md)
- [HistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/HistoryResponse.md)

### Transaction information

- [Get-Transaction-Info](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-Info.md)
- [TransactionInfoResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/TransactionInfoResponse.md)

### App Transaction information

- [Get-App-Transaction-Info](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-App-Transaction-Info.md)
- [AppTransactionInfoResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionInfoResponse.md)

### Subscription status

- [Get-All-Subscription-Statuses](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-All-Subscription-Statuses.md)
- [StatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/StatusResponse.md)

### App Account Token

- [Set-App-Account-Token](../com.apple.appstoreserverapi/AppStoreServerAPI/Set-App-Account-Token.md)
- [UpdateAppAccountTokenRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/UpdateAppAccountTokenRequest.md)

### Order ID lookup

- [Look-Up-Order-ID](../com.apple.appstoreserverapi/AppStoreServerAPI/Look-Up-Order-ID.md)
- [orderId](../com.apple.appstoreserverapi/AppStoreServerAPI/orderId.md)
- [OrderLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/OrderLookupResponse.md)

### Consumption information

- [Send-Consumption-Information](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information.md)
- [ConsumptionRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequest.md)

### Refund lookup

- [Get-Refund-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History.md)
- [RefundHistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundHistoryResponse.md)

### Subscription-renewal-date extension

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

### App Store Server Notifications history

- [Get-Notification-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Notification-History.md)
- [NotificationHistoryRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryRequest.md)
- [NotificationHistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryResponse.md)
- [notificationHistoryResponseItem](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationHistoryResponseItem.md)

### App Store Server Notifications testing

- [Request-a-Test-Notification](../com.apple.appstoreserverapi/AppStoreServerAPI/Request-a-Test-Notification.md)
- [Get-Test-Notification-Status](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Test-Notification-Status.md)
- [SendTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/SendTestNotificationResponse.md)
- [CheckTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/CheckTestNotificationResponse.md)

### JWS headers and payloads

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

### Error information

- [error-codes](../com.apple.appstoreserverapi/AppStoreServerAPI/error-codes.md)

### Deprecated

- [Get-Transaction-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History-V1.md)
- [Get-Refund-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History-V1.md)
- [Send-Consumption-Information-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information-V1.md)
- [ConsumptionRequestV1](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequestV1.md)
- [RefundLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundLookupResponse.md)

---


# Detailed Documentation


## AdvancedCommerceTransactionNotSupportedError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AdvancedCommerceTransactionNotSupportedError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## AppNotFoundError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AppNotFoundError
```

## 

Check the `bid` claim in the JSON Web Token (JWT) to make sure that your app’s bundle ID is correct. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests).

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## AppNotFoundRetryableError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AppNotFoundRetryableError
```

## See Also

- [AccountNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundRetryableError.md)
- [GeneralInternalRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalRetryableError.md)
- [OriginalTransactionIdNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/OriginalTransactionIdNotFoundRetryableError.md)

---


## AppTransactionDoesNotExistError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AppTransactionDoesNotExistError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## AppTransactionInfoResponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AppTransactionInfoResponse
```

## 

This response contains information that you request by calling the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info) endpoint. For information on decoding and reading the app transaction, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransaction](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransaction) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload).

## Topics

### Response data types

- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)

## See Also

- [Get-App-Transaction-Info](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-App-Transaction-Info.md)

---


## ConsumptionPercentageOutOfRangeError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ConsumptionPercentageOutOfRangeError
```

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## ConsumptionRequest

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ConsumptionRequest
```

## 

Use `ConsumptionRequest` to provide information about the customer’s In-App Purchase when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) endpoint.

> **NOTE:** The App Store server rejects requests that have a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented) value other than `true` by returning an `HTTP 400` error with an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidCustomerConsentedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidCustomerConsentedError).

You can provide consumption information for any type of product: consumable, non-consumable, non-renewing subscription, and auto-renewable subscription.

Consider the following constraints when providing an optional [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest/refundPreference](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest/refundPreference):

- The system supports the `GRANT_FULL` and `DECLINE` values for all product types.
- If you choose `GRANT_PRORATED` for an auto-renewable subscription, don’t include a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest/consumptionPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest/consumptionPercentage). The system automatically calculates the percentage.

If the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest/deliveryStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest/deliveryStatus) isn’t `DELIVERED`, set the `consumptionPercentage` to `0`; otherwise the request fails with an error.

## Topics

### Consumption data types

- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [consumptionPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionPercentage.md)
- [deliveryStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatus.md)
- [refundPreference](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreference.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)

## See Also

- [Send-Consumption-Information](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information.md)

---


## ConsumptionRequestV1

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ConsumptionRequestV1
```

## 

Use `ConsumptionRequestV1` to provide information about the customer’s consumable in-app purchase or auto-renewable subscription when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) endpoint.

To create a valid request and avoid an `HTTP 400 Bad Request` error, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) must contain all the required fields with proper data types and valid values. However, you can choose whether or not to provide information for most fields. Most fields have a valid option if you choose not to provide the information.

> **NOTE:** Use the field value for *undeclared*, where available, if you choose not to provide information.

For example, if you choose not to provide information for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/accountTenure](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/accountTenure) field, set [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/accountTenure](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/accountTenure) to `0`. If you choose not to provide information for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken) field, set its value to an empty string. Refer to each field’s documentation for the list of valid values, including the undeclared value where available.

The App Store server rejects requests that have a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented) value other than `true` by returning an `HTTP 400` error with an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidCustomerConsentedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidCustomerConsentedError).

### 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) request body requires that you set the `appAccountToken` to a valid value of either a UUID or an empty string. Set the `appAccountToken` value to the value you received in the `CONSUMPTION_REQUEST` notification, or, if you choose not to provide this information, set the value to an empty string.

If you receive a `CONSUMPTION_REQUEST` notification for a transaction, find its associated `appAccountToken` value as follows:

- If you receive [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2), the `appAccountToken` value is in [doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload).
- If you receive [doc://com.apple.documentation/documentation/AppStoreServerNotifications/app-store-server-notifications-version-1](doc://com.apple.documentation/documentation/AppStoreServerNotifications/app-store-server-notifications-version-1), the `appAccountToken` value is in [doc://com.apple.documentation/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary](doc://com.apple.documentation/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary).

The `appAccountToken` value may be an empty string if your app doesn’t use app account tokens.

For more information about App Store Server Notifications versions, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog](doc://com.apple.documentation/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).

## Topics

### Consumption data types

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

## See Also

- [Get-Transaction-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History-V1.md)
- [Get-Refund-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History-V1.md)
- [Send-Consumption-Information-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information-V1.md)
- [RefundLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundLookupResponse.md)

---


## Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers

## 

Use this endpoint to compensate your customers for temporary service outages, canceled events, or interruptions to live streamed events by extending the renewal date of their paid, active subscription. This endpoint acts on all active subscriptions for the product identifier you specify, and is limited to the storefronts you optionally specify.

To call this endpoint, provide the subscription product identifier that experienced the service interruption, and other information, in the request body, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest).

A successful response with an `HTTP 200` status code contains the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateResponse) object, which includes the same unique `requestIdentifier` you provide in the request. This endpoint is an asynchronous request. A successful response indicates that the App Store server is processing the request. Status codes other than `HTTP 200` indicate that the request failed.

> **NOTE:** After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

After a successful renewal date extension, Apple sends an email to notify the customer of their updated subscription renewal date.

For more information about this endpoint, including subscription eligibility, getting status notifications, and retrying extensions that fail, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## FamilySharedSubscriptionExtensionIneligibleError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object FamilySharedSubscriptionExtensionIneligibleError
```

## 

A request returns this error if you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint with an `originalTransactionId` that belongs to a subscription the user obtains through Family Sharing.

When the endpoint extends an eligible purchased subscription that supports Family Sharing, it automatically extends the family members’ subscriptions as well. However, the endpoint doesn’t support requests to extend a family member’s subscription directly.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## GeneralBadRequestError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object GeneralBadRequestError
```

## 

A bad request error typically occurs when the server receives a malformed request or a request that contains incorrect syntax.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## GeneralInternalRetryableError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object GeneralInternalRetryableError
```

## See Also

- [AccountNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundRetryableError.md)
- [AppNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundRetryableError.md)
- [OriginalTransactionIdNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/OriginalTransactionIdNotFoundRetryableError.md)

---


## Get-All-Subscription-Statuses

## 

This API returns the status for all of the customer’s subscriptions, organized by their subscription group identifier.

Specify multiple values for the `status` query parameter to get a response that contains subscriptions with statuses that match any of the values. For example, the following request returns subscriptions that are active ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses/status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses/status) value of `1`) and subscriptions that are in the Billing Grace Period ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses/status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses/status) value of `4`):

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/subscriptions/{transactionId}?status=1&status=4
```

## See Also

- [StatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/StatusResponse.md)

---


## Get-Notification-History

## 

Call this endpoint to get a paginated list of the version 2 [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications) that the App Store attempted to send to your server’s [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint in a specified timespan. Notification history is available for the past 180 days in the production environment, and the past 30 days in the sandbox environment.

You can further limit the request by specifying a `notificationType` or `notificationSubtype` in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest) object. Alternatively, to get the notification history for a single user, provide a `transactionId`. The response, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse), contains the full contents of the original notifications.

Each time you call this endpoint, it returns a maximum of 20 notification history records. If the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore) field in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse) is `true`, use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History/paginationToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History/paginationToken) from the response in your subsequent request to get the next set of records. Use the same [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest) body on subsequent requests.

This endpoint is available in the production and sandbox environments. For more information about configuring App Store Server Notifications, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications) and [https://help.apple.com/app-store-connect/#/dev0067a330b](https://help.apple.com/app-store-connect/#/dev0067a330b).

> **NOTE:** For notifications that relate to in-app purchases, the history records reflect the state of an in-app purchase at the time the App Store originally sent the notification, and may not reflect its current state. To get the current state of auto-renewable subscriptions, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses) endpoint. For all other in-app purchase types, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint.

## See Also

- [NotificationHistoryRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryRequest.md)
- [NotificationHistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryResponse.md)
- [notificationHistoryResponseItem](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationHistoryResponseItem.md)

---


## Get-Refund-History-V1

## 

Call this endpoint to get a customer’s refund history for your app. The response ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundLookupResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundLookupResponse)) includes up to 50 of the customer’s most-recently refunded transactions, based on the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationDate).

> **NOTE:** To get the complete refund history, use [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History).

To call this endpoint, provide any original transaction identifier ([doc://com.apple.documentation/documentation/StoreKit/Transaction/originalID](doc://com.apple.documentation/documentation/StoreKit/Transaction/originalID)) for any of the customer’s in-app purchases. The response only includes App Store-approved refunds for any product type: consumable, non-consumable, auto-renewable subscriptions, and non-renewing subscriptions. For more information about product types, see [https://developer.apple.com/in-app-purchase/](https://developer.apple.com/in-app-purchase/).

The information in the response is the same as the information in one or more `REFUND` notifications ([doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType)) from [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications). Use this API to retrieve any refund notifications you may have missed, such as during a server outage.

A successful response may have an empty `signedTransactions` array if the customer hasn’t received any App Store-approved refunds. To identify the date and reason code for a refund, see `revocationDate` and `revocationReason` in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload).

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

## See Also

- [Get-Transaction-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History-V1.md)
- [Send-Consumption-Information-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information-V1.md)
- [ConsumptionRequestV1](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequestV1.md)
- [RefundLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundLookupResponse.md)

---


## Get-Refund-History

## 

Call this endpoint to get the customer’s complete refund history for your app by providing the transaction identifier ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History/transactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History/transactionId)) for any of the customer’s in-app purchases. Each response ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse)) contains a maximum of 20 refunded transactions. If the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore) property in the response is `true`, call the endpoint again using the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History/revision) token from the response to get the next set of refunded transactions.

The response only includes App Store-approved refunds for any product type: consumable, non-consumable, auto-renewable subscriptions, and non-renewing subscriptions. For more information about product types, see [https://developer.apple.com/in-app-purchase/](https://developer.apple.com/in-app-purchase/).

The information in the response is the same as the information in one or more `REFUND` notifications ([doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType)) from [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications). Use this API to retrieve any refund notifications you may have missed, such as during a server outage.

A successful response may have an empty `signedTransactions` array if the customer hasn’t received any App Store-approved refunds. To identify the date and reason code for a refund, see `revocationDate` and `revocationReason` in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload).

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installs, removes, or reinstalls the app on their devices.

To get a customer’s full refund history for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/refund/lookup/{transactionId}
```

For subsequent requests, include the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History/revision) token from the previous [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse).

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/refund/lookup/{transactionId}?revision={revision}
```

## See Also

- [RefundHistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundHistoryResponse.md)

---


## Get-Status-of-Subscription-Renewal-Date-Extensions

## 

This endpoint provides basic status information about a request you initiate when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint. Such requests may take hours, or even days, depending on the number of subscribers. This status tells whether the request is complete. If so, it has the total count of successful and failed subscription-renewal-date extensions.

> **TIP:** If you don’t need this status on demand, or need more details, use the [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications) for near real-time status information instead. For more information about related notifications, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## InvalidEndDateError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidEndDateError
```

## See Also

- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## InvalidExcludeRevokedError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidExcludeRevokedError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)

---


## InvalidLifetimeDollarsRefundedError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidLifetimeDollarsRefundedError
```

## 

For valid `lifetimeDollarsRefunded` values in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/lifetimeDollarsRefunded](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/lifetimeDollarsRefunded).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## InvalidNotificationTypeError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidNotificationTypeError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## InvalidOriginalTransactionIdError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidOriginalTransactionIdError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## InvalidPlatformError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidPlatformError
```

## 

For valid `platform` values in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/platform](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/platform).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## InvalidPlayTimeError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidPlayTimeError
```

## 

For valid `playTime` values in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/playTime](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/playTime).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## InvalidProductTypeError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidProductTypeError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## InvalidRequestIdentifierError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidRequestIdentifierError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier) you provide in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoints.

For the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoints, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier) needs to be a `UUID`.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## InvalidRequestRevisionError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidRequestRevisionError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revision) query parameter of endpoints like [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History).

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## InvalidStorefrontCountryCodeError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidStorefrontCountryCodeError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefrontCountryCodes](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefrontCountryCodes) list you provide in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest) object for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## InvalidSubscriptionGroupIdentifierError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidSubscriptionGroupIdentifierError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## InvalidTransactionTypeNotSupportedError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidTransactionTypeNotSupportedError
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) endpoint returns this error if the `transactionId` doesn’t represent a supported in-app purchase. Be sure to provide the same `transactionId` that you receive to your [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint in a notification with a `CONSUMPTION_REQUEST` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## InvalidUserStatusError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidUserStatusError
```

## 

For valid `userStatus` values in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/userStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/userStatus).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## JWSDecodedHeader

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object JWSDecodedHeader
```

## 

The types [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransaction](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransaction) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfo](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfo) contain headers that are [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader) objects when decoded. Use the information in the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSDecodedHeader](doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSDecodedHeader) to validate the JWS signature. For more information about validating signatures, see the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The App Store signs transaction and renewal information that you receive in [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) and in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI). It uses the following `x5c` certificate chain, in the following order:

1. A certificate that contains the public key that corresponds to the key the App Store uses to digitally sign the JWS. Section 4.11.10 Mac App Store Receipt Signing Certificates of the [https://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf](https://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf) document defines the custom extensions this certificate uses.
2. An Apple intermediate certificate that contains an extension with the extension ID for `Apple Worldwide Developer Relations (1.2.840.113635.100.6.2.1)`.
3. An Apple root certificate.

For more information, or to download Apple’s root certificate, see [https://www.apple.com/certificateauthority/](https://www.apple.com/certificateauthority/).

## Topics

### Data types

- [alg](../com.apple.appstoreserverapi/AppStoreServerAPI/alg.md)
- [x5c](../com.apple.appstoreserverapi/AppStoreServerAPI/x5c.md)

## See Also

- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## JWSRenewalInfoDecodedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object JWSRenewalInfoDecodedPayload
```

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## JWSTransaction

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string JWSTransaction
```

## 

The `JWSTransaction` type is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the transaction information, signed by the App Store according to the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

- To read the transaction information, Base64URL-decode the payload. Use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) object to read the payload information.
- To read the header, decode it and use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader) object to access the information. Use the information in the header to verify the signature.

### 

To verify a `JWSTransaction` on your server, consider implementing the verification using the App Store Server Library function `verifyAndDecodeTransaction`. The library provides this function in each language the library supports. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## JWSTransactionDecodedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object JWSTransactionDecodedPayload
```

## 

> **IMPORTANT:** Don’t use the `price` or `currency` values for any revenue reconciliation or recognition. App Store Connect reporting is your source of record for financial and accounting purposes. For more information, see [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## MultipleFiltersSuppliedError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object MultipleFiltersSuppliedError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## NotificationHistoryRequest

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object NotificationHistoryRequest
```

## 

Specify the constraints for the App Store Server Notification history entries you’re requesting from [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History). The request requires the `startDate` and `endDate` fields; all other fields are optional. Include only the fields in your request that you need to constrain the response.

If you provide both the `notificationType` and `subtype`, they need to be a valid combination, otherwise, the request returns an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidNotificationTypeError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidNotificationTypeError) error. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) and [doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype](doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype).

> **NOTE:** Notification history is available for the past 180 days in the production environment, and the past 30 days in the sandbox environment. Choose a `startDate` that’s within the past 180 days in the production environment, and within the past 30 days in the sandbox environment.

## Topics

### Data types

- [startDate](../com.apple.appstoreserverapi/AppStoreServerAPI/startDate.md)
- [endDate](../com.apple.appstoreserverapi/AppStoreServerAPI/endDate.md)
- [notificationType](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationType.md)
- [notificationSubtype](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationSubtype.md)
- [onlyFailures](../com.apple.appstoreserverapi/AppStoreServerAPI/onlyFailures.md)

## See Also

- [Get-Notification-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Notification-History.md)
- [NotificationHistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryResponse.md)
- [notificationHistoryResponseItem](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationHistoryResponseItem.md)

---


## NotificationHistoryResponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object NotificationHistoryResponse
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) endpoint returns this response. Notification history records contain the notifications that the App Store server attempted to send to your server’s [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint.

The notification history response contains a maximum of 20 notification history records per response. If the history has more than 20 records, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse/hasMore) value is `true`. Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) again with `paginationToken` in the query to receive the next page of responses. When the App Store has no more records to send, the `hasMore` value is `false`.

> **NOTE:** The notifications in the history records reflect the state of an in-app purchase at the time the App Store originally sent the notification, and may not reflect its current state. To get the current state of auto-renewable subscriptions, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses) endpoint. For all other in-app purchase types, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint.

## Topics

### Data types

- [paginationToken](../com.apple.appstoreserverapi/AppStoreServerAPI/paginationToken.md)
- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)

## See Also

- [Get-Notification-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Notification-History.md)
- [NotificationHistoryRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryRequest.md)
- [notificationHistoryResponseItem](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationHistoryResponseItem.md)

---


## OriginalTransactionIdNotFoundError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object OriginalTransactionIdNotFoundError
```

## 

Don’t unlock the service or content associated with the transaction ID for the app bundle ID and environment that you indicate in the request unless you successfully resolve this error. To resolve this error, check your request to ensure that:

- The JSON Web Token (JWT) payload contains the bundle ID (`bid`) of your app that’s associated with the transaction ID. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests).
- You’re making the request in the same environment, production or sandbox, that generated the transaction ID.

In rare cases, you might get this error for transaction IDs that previously returned data successfully. Don’t unlock the service or content for the app bundle ID and environment in the request if you’re unable to resolve this error using the steps above.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## OriginalTransactionIdNotFoundRetryableError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object OriginalTransactionIdNotFoundRetryableError
```

## See Also

- [AccountNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundRetryableError.md)
- [AppNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundRetryableError.md)
- [GeneralInternalRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalRetryableError.md)

---


## PaginationTokenExpiredError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object PaginationTokenExpiredError
```

## 

When calling [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History), use the same [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest) body on subsequent page requests that include a pagination token in the query.

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## RefundLookupResponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object RefundLookupResponse
```

## 

If the customer hasn’t received any refunds for in-app purchases in your app, the `signedTransactions` array is empty. To read the transaction information, decode the payload for each [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransaction](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransaction) object in the `signedTransactions` array. Use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) object to read the transaction information in the payload.

This response can contain a maximum of 50 transactions in the `signedTransactions` array.

## See Also

- [Get-Transaction-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History-V1.md)
- [Get-Refund-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History-V1.md)
- [Send-Consumption-Information-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information-V1.md)
- [ConsumptionRequestV1](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequestV1.md)

---


## ServerNotificationURLNotFoundError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ServerNotificationURLNotFoundError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## Set-App-Account-Token

## 

An [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken) is a UUID you create to associate a transaction with a customer account in your system. Use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token) endpoint to set or reset the `appAccountToken` associated with the transaction you specify in the `originalTransactionId` parameter.

Typically, your app sets the [doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)](doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) when a customer makes a purchase in your app. However, customers can also purchase in-app products outside of your app, for example, by redeeming an offer code in the App Store. In that case, the original transaction doesn’t include an app account token. Use the `Set App Account Token` endpoint to associate an app account token with such transactions.

This endpoint supports setting the `appAccountToken` for all product types, including one-time purchases (consumables, non-consumables, and non-renewing subscriptions) and auto-renewable subscriptions. If you call this endpoint for a transaction that already has an `appAccountToken`, the endpoint replaces the existing value with the new value you supply.

For auto-renewable subscriptions, the endpoint applies the `appAccountToken` to the current renewal transaction and subsequent renewals, but it doesn’t affect past transactions. The same `appAccountToken` continues to apply to renewal transactions if the customer upgrades, downgrades, or cross-grades the subscription.

This endpoint doesn’t support transactions for products shared through Family Sharing, where the transaction has an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/inAppOwnershipType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/inAppOwnershipType) value of `FAMILY_SHARED`.

You can assign the same `appAccountToken` value to more than one transaction, according to your needs. For example, you may choose to reuse the same `appAccountToken` value for every transaction that belongs to the same customer.

## See Also

- [UpdateAppAccountTokenRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/UpdateAppAccountTokenRequest.md)

---


## StartDateTooFarInPastError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object StartDateTooFarInPastError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## StatusRequestNotFoundError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object StatusRequestNotFoundError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoint. Check that the `productId` and `requestIdentifier` parameters match the values associated with your request to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## StatusResponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object StatusResponse
```

## Topics

### Response Objects and Data Types

- [SubscriptionGroupIdentifierItem](../com.apple.appstoreserverapi/AppStoreServerAPI/SubscriptionGroupIdentifierItem.md)
- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)

## See Also

- [Get-All-Subscription-Statuses](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-All-Subscription-Statuses.md)

---


## SubscriptionGroupIdentifierItem

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object SubscriptionGroupIdentifierItem
```

## Topics

### Object and Data Types

- [subscriptionGroupIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/SubscriptionGroupIdentifierItem/subscriptionGroupIdentifier.md)
- [lastTransactionsItem](../com.apple.appstoreserverapi/AppStoreServerAPI/lastTransactionsItem.md)

## See Also

- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)

---


## SubscriptionMaxExtensionError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object SubscriptionMaxExtensionError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## TransactionIdIsNotOriginalTransactionIdError

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object TransactionIdIsNotOriginalTransactionIdError
```

## 

Not all transaction identifiers are original transaction identifiers. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId).

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## TransactionInfoResponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object TransactionInfoResponse
```

## 

The `TransactionInfoResponse` contains information about the transaction that you request using the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info) endpoint. The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId) in the `signedTransactionInfo` matches the `transactionId` you provide in the request path.

## Topics

### Response data types

- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

## See Also

- [Get-Transaction-Info](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-Info.md)

---


## accountTenure

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 accountTenure
```

## See Also

- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## accountnotfounderror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AccountNotFoundError
```

## See Also

- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## accountnotfoundretryableerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AccountNotFoundRetryableError
```

## See Also

- [AppNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundRetryableError.md)
- [GeneralInternalRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalRetryableError.md)
- [OriginalTransactionIdNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/OriginalTransactionIdNotFoundRetryableError.md)

---


## advancedCommerceConsistencyToken

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceConsistencyToken
```

## See Also

- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommerceDescription

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceDescription
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommerceDescriptors

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceDescriptors
```

## See Also

- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedCommerceEstimatedTax

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 advancedCommerceEstimatedTax
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommerceOfferPrice

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 advancedCommerceOfferPrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommercePeriod

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommercePeriod
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommercePrice

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 advancedCommercePrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommercePriceIncreaseInfo

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommercePriceIncreaseInfo
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedCommercePriceIncreaseInfoDependentSKU

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommercePriceIncreaseInfoDependentSKU
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommercePriceIncreaseInfoPrice

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 advancedCommercePriceIncreaseInfoPrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommerceRefund

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceRefund
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedCommerceRefundAmount

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 advancedCommerceRefundAmount
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommerceRefundDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp advancedCommerceRefundDate
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedCommerceRefundType

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceRefundType
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedCommerceRenewalItem

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceRenewalItem
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedCommerceRequestReferenceId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceRequestReferenceId
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedCommerceSKU

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceSKU
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedCommerceTaxExclusivePrice

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 advancedCommerceTaxExclusivePrice
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedCommerceTaxRate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceTaxRate
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedCommerceTransactionInfo

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceTransactionInfo
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedCommerceTransactionItem

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceTransactionItem
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)

---


## advancedCommerceTransactionItems

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
[advancedCommerceTransactionItem] advancedCommerceTransactionItems
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedcommerce-datatypes

## 

For more information about [doc://com.apple.documentation/documentation/AdvancedCommerceAPI](doc://com.apple.documentation/documentation/AdvancedCommerceAPI), see [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/).

## Topics

### Data types

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)
- [advancedCommerceRefundType](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundType.md)
- [advancedCommerceRefunds](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefunds.md)
- [advancedCommerceRenewalItems](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItems.md)
- [advancedCommerceRequestReferenceId](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRequestReferenceId.md)
- [advancedCommerceSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceSKU.md)
- [advancedCommerceTaxCode](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTaxCode.md)
- [advancedCommerceTaxExclusivePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTaxExclusivePrice.md)
- [advancedCommerceTaxRate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTaxRate.md)
- [advancedCommerceTransactionItems](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItems.md)

### Objects

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedcommercedisplayname

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceDisplayName
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedcommerceoffer

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceOffer
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalInfo.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedcommerceofferperiod

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceOfferPeriod
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedcommerceperiodcount

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 advancedCommercePeriodCount
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedcommercepriceincreaseinfostatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommercePriceIncreaseInfoStatus
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedcommercereason

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceReason
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)
- [advancedCommerceRefundReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundReason.md)

---


## advancedcommercerefundreason

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceRefundReason
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedcommercerefunds

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
[advancedCommerceRefund] advancedCommerceRefunds
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedcommercerenewalinfo

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object advancedCommerceRenewalInfo
```

## See Also

- [advancedCommerceDescriptors](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescriptors.md)
- [advancedCommerceOffer](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOffer.md)
- [advancedCommercePriceIncreaseInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfo.md)
- [advancedCommerceRefund](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefund.md)
- [advancedCommerceRenewalItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRenewalItem.md)
- [advancedCommerceTransactionInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionInfo.md)
- [advancedCommerceTransactionItem](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceTransactionItem.md)

---


## advancedcommercerenewalitems

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
[advancedCommerceRenewalItem] advancedCommerceRenewalItems
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## advancedcommercetaxcode

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string advancedCommerceTaxCode
```

## See Also

- [advancedCommerceConsistencyToken](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceConsistencyToken.md)
- [advancedCommerceDescription](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDescription.md)
- [advancedCommerceDisplayName](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceDisplayName.md)
- [advancedCommerceEstimatedTax](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceEstimatedTax.md)
- [advancedCommerceOfferPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPeriod.md)
- [advancedCommerceOfferPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceOfferPrice.md)
- [advancedCommercePeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriod.md)
- [advancedCommercePeriodCount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePeriodCount.md)
- [advancedCommercePrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePrice.md)
- [advancedCommercePriceIncreaseInfoDependentSKU](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU.md)
- [advancedCommercePriceIncreaseInfoPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice.md)
- [advancedCommercePriceIncreaseInfoStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus.md)
- [advancedCommerceReason](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceReason.md)
- [advancedCommerceRefundAmount](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundAmount.md)
- [advancedCommerceRefundDate](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedCommerceRefundDate.md)

---


## alg

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string alg
```

## See Also

- [x5c](../com.apple.appstoreserverapi/AppStoreServerAPI/x5c.md)

---


## app-store-server-api-changelog

## 

Use this changelog to learn about feature updates, deprecations, and removals for the App Store Server API.

### 

**New features**

- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) endpoint.
- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationType) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationPercentage) fields to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload).
- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfo](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfo) object, and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfoDependentSKU), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfoStatus), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/advancedCommercePriceIncreaseInfoPrice), fields to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload).

**Deprecations**

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) endpoint is deprecated. Use the new [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) endpoint instead.

### 

**New features**

- Added the `ONE_TIME` value to [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerDiscountType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerDiscountType) to indicate In-App Purchase offer codes.

### 

**New features**

- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info) endpoint and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/AppTransactionInfoResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/AppTransactionInfoResponse) response object.

### 

**New features**

- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token) endpoint and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/UpdateAppAccountTokenRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/UpdateAppAccountTokenRequest) request object, and related error codes:  [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionIdIsNotOriginalTransactionIdError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionIdIsNotOriginalTransactionIdError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/FamilyTransactionNotSupportedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/FamilyTransactionNotSupportedError), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidAppAccountTokenUUIDError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidAppAccountTokenUUIDError).

### 

**New features**

- Updated the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) to include the new [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appTransactionId) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerPeriod](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerPeriod) fields.
- Updated the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) to include the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken) field.
- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/AppTransactionIdNotSupportedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/AppTransactionIdNotSupportedError) error object.

### 

**New features**

- Added support for [doc://com.apple.documentation/documentation/AdvancedCommerceAPI](doc://com.apple.documentation/documentation/AdvancedCommerceAPI).

### 

**New features**

- Updated the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) to include the new [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/eligibleWinBackOfferIds](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/eligibleWinBackOfferIds) field.
- Added the win-back offer type in [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerType).

### 

**New features**

- Added the endpoint [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History), which provides transaction history for all In-App Purchases, including consumable In-App Purchases in a finished state.
- Added the fields [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalPrice](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalPrice), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerDiscountType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerDiscountType) to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload).

**Deprecations**

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) endpoint is deprecated. Use the new [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint instead.

### 

New features

- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreferenceV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreferenceV1) field to the  [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) request body.
- [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) added  support for receiving information for auto-renewable subscriptions.
- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError) error object.

**Deprecations**

- The system no longer sends the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionNotConsumableError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionNotConsumableError) error object. It uses [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError) instead.

### 

- The type of the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/price](doc://com.apple.documentation/documentation/AppStoreServerNotifications/price) field changed from `int32` to `int64`.

### 

**New features**

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) endpoint adds support for the new notification type for unreported external purchase tokens.

### 

New features

- Added the following new properties in the decoded transaction payload [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload): [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/price](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/price), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerDiscountType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerDiscountType).

### 

New features

- Updated the error format of the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) endpoint to match that of other endpoints. The endpoint now returns a JSON body that can contain an error code.
- New error codes for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) endpoint include: [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidAccountTenureError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidAccountTenureError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidAppAccountTokenError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidAppAccountTokenError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidConsumptionStatusError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidConsumptionStatusError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidCustomerConsentedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidCustomerConsentedError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidDeliveryStatusError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidDeliveryStatusError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidPlatformError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidPlatformError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidPlayTimeError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidPlayTimeError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidSampleContentProvidedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidSampleContentProvidedError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionNotConsumableError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionNotConsumableError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidUserStatusError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidUserStatusError).

### 

New features

- Added a new endpoint [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info) with its response  [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionInfoResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionInfoResponse), which provides information about a single transaction.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) endpoint adds a new filter parameter, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/onlyFailures](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/onlyFailures). When you set it to `true`, the endpoint returns only the notifications that failed to reach the developer’s server.
- The following endpoints changed their path parameters from [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId) to [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId): [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1). These endpoints now accept any transaction identifier, including original transaction identifiers.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) endpoint now accepts a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionId) instead of requiring an original transaction identifier ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId)) in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryRequest) body.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) endpoint adds a new filter parameter, `revoked`, that filters the response to return only revoked transactions or only nonrevoked transactions.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses) endpoint adds a new filter parameter, `status`, that enables you to request subscriptions with the status values you specify.
- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefrontId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefrontId), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionReason](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/transactionReason) fields to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) object.
- Added the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalDate) field to the  [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) object.
- Added the `sendAttempts` field to the  [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/CheckTestNotificationResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/CheckTestNotificationResponse) and the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/notificationHistoryResponseItem](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/notificationHistoryResponseItem) of the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse) to provide information about all the send attempts for App Store Server Notifications.
- Added the error codes [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/StatusRequestNotFoundError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/StatusRequestNotFoundError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidStatusError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidStatusError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidRevokedError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidRevokedError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionIdError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/InvalidTransactionIdError), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionIdNotFoundError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/TransactionIdNotFoundError),  and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError).
- All endpoints are subject to a rate limit and can return a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError) with an HTTP 429 error code. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/identifying-rate-limits](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/identifying-rate-limits).

**Deprecations**

- The `excludeRevoked` filter in [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) is deprecated. Use the new `revoked` filter instead.
- The `firstSendAttemptResult` field is deprecated in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/CheckTestNotificationResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/CheckTestNotificationResponse) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/notificationHistoryResponseItem](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/notificationHistoryResponseItem) objects. Use the first [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptItem](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptItem) in the `sendAttempts` array instead.

### 

New features

- The new endpoint [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) takes a subscription product identifier and extends the renewal date for all eligible subscribers. It responds with [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateResponse). For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions). For information about new App Store server notifications related to this endpoint, see the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog](doc://com.apple.documentation/documentation/AppStoreServerNotifications/app-store-server-notifications-changelog).
- The new endpoint [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) checks the status of a subscription-renewal-date extension, and responds with the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateStatusResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateStatusResponse).

### 

New features

- The new version 2 endpoint [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History) returns a paginated list of refunded transactions in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse).

Deprecations

- The endpoint [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1) and its response [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundLookupResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundLookupResponse) are deprecated.
- In `firstSendAttemptResult`, the `SSL_ISSUE` value is deprecated and replaced with `TLS_ISSUE`.

### 

New features

- The API has two new endpoints to support testing how your server receives App Store Server Notifications. The endpoints are: [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status).
- The API adds the new [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) endpoint.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) endpoint is enhanced with new parameters to support filtering and sorting functionality.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) now includes the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/recentSubscriptionStartDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/recentSubscriptionStartDate) field.

### 

This version doesn’t contain any public changes.

### 

This version doesn’t contain any public changes.

### 

Removals

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader) object no longer includes the `kid` field.

### 

New features

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) objects now include the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/environment](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/environment) field.

### 

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1) endpoint now returns a maximum of 50 refunded transactions.

### 

New features

- The API adds three endpoints: [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date).

### 

The API is now available in the production environment, using the following base URL:

```other
https://api.storekit.itunes.apple.com/inApps/
```

### 

Initial version of the App Store Server API.

New features

- This API has three endpoints, available in the sandbox environment: [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses).

## See Also

- [simplifying-your-implementation-by-using-the-app-store-server-library](../com.apple.appstoreserverapi/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library.md)
- [creating-api-keys-to-authorize-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
- [generating-json-web-tokens-for-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
- [identifying-rate-limits](../com.apple.appstoreserverapi/AppStoreServerAPI/identifying-rate-limits.md)

---


## appAccountToken

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
uuid appAccountToken
```

## 

When a customer initiates an In-App Purchase in your app, you can optionally generate an app account token and call [doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)](doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) to associate it with the purchase. If you use the [doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase), you can provide a UUID in the [doc://com.apple.documentation/documentation/StoreKit/SKMutablePayment/applicationUsername](doc://com.apple.documentation/documentation/StoreKit/SKMutablePayment/applicationUsername) property. The App Store returns the same UUID in [doc://com.apple.documentation/documentation/StoreKit/Transaction/appAccountToken](doc://com.apple.documentation/documentation/StoreKit/Transaction/appAccountToken) in the transaction information and subscription renewal information after the customer completes the purchase.

To provide an app account token for a transaction that the customer completes outside of your app, or to update the value of an existing app account token, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token) endpoint.

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## appappleid

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 appAppleId
```

## See Also

- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)
- [revision](../com.apple.appstoreserverapi/AppStoreServerAPI/revision.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

---


## apptransactionid

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string appTransactionId
```

## 

To get app transaction information, call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info) and provide the `appTransactionId`.

For more information, see [doc://com.apple.documentation/documentation/StoreKit/AppTransaction/appTransactionID](doc://com.apple.documentation/documentation/StoreKit/AppTransaction/appTransactionID).

---


## apptransactionidnotsupportederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object AppTransactionIdNotSupportedError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## attemptdate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp attemptDate
```

## See Also

- [sendAttemptResult](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptResult.md)

---


## autoRenewProductId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string autoRenewProductId
```

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## autorenewstatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 autoRenewStatus
```

## See Also

- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## bundleId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string bundleId
```

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)
- [revision](../com.apple.appstoreserverapi/AppStoreServerAPI/revision.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

---


## checktestnotificationresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object CheckTestNotificationResponse
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status) endpoint returns this response.

The `sendAttempts` array contains up to six [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptItem](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptItem) items: one for the initial attempt, and up to five for the retries. Use this information to troubleshoot your server if it doesn’t receive notifications at its [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint successfully.

The `signedPayload` contains the `TEST` notification that the App Store server attempted to send to your server.

## Topics

### Data types

- [sendAttemptItem](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptItem.md)
- [signedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/signedPayload.md)

## See Also

- [Request-a-Test-Notification](../com.apple.appstoreserverapi/AppStoreServerAPI/Request-a-Test-Notification.md)
- [Get-Test-Notification-Status](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Test-Notification-Status.md)
- [SendTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/SendTestNotificationResponse.md)

---


## complete

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean complete
```

## 

The request is complete when this value is `TRUE`. For more information about the subscription-renewal-date extension, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers).

## See Also

- [completeDate](../com.apple.appstoreserverapi/AppStoreServerAPI/completeDate.md)
- [failedCount](../com.apple.appstoreserverapi/AppStoreServerAPI/failedCount.md)
- [succeededCount](../com.apple.appstoreserverapi/AppStoreServerAPI/succeededCount.md)

---


## completedate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp completeDate
```

## 

For more information about a requesting a subscription-renewal-date extension, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers).

## See Also

- [complete](../com.apple.appstoreserverapi/AppStoreServerAPI/complete.md)
- [failedCount](../com.apple.appstoreserverapi/AppStoreServerAPI/failedCount.md)
- [succeededCount](../com.apple.appstoreserverapi/AppStoreServerAPI/succeededCount.md)

---


## consumptionPercentage

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 consumptionPercentage
```

## 

You can provide a consumption percentage in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest) object when you call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) for consumable and non-consumable In-App Purchases and non-renewing subscriptions. The consumption percentage represents the portion of the product that the customer consumed.

The consumption percentage you provide is one of a variety of factors that the App Store uses to inform its refund decisions. The final refund percentage may differ from the value you provide.

Consider the following when you use this field:

- If you select `GRANT_PRORATED` for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreference](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreference) field, you need to provide a `consumptionPercentage` greater than `0` and less than `100000`.
- If the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/deliveryStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/deliveryStatus) value isn’t `DELIVERED`, set the `consumptionPercentage` to `0`; otherwise, the request fails with an `HTTP 400` error [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError).
- Don’t provide a consumption percentage for auto-renewable subscriptions, otherwise the request fails with an `HTTP 400` error [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError). The system automatically calculates the consumption percentage for auto-renewable subscriptions based on elapsed time.

Use the consumption percentage to indicate the amount of the product the customer consumed. The percentage value allows for three decimal places of precision, and is expressed as an integer, in milliunits. The following table shows several examples of valid consumption percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
| --- | --- |
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

For example, if a transaction contains a quantity of two consumable In-App Purchases, and the customer fully consumed one of them, the `consumptionPercentage` is `50000`, which represents 50%.

If the system approves a prorated refund, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationPercentage) field in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) contains the revoked percentage of the transaction.

## See Also

- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatus.md)
- [refundPreference](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreference.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)

---


## consumptionStatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 consumptionStatus
```

## 

Some examples of consumption status include the following scenarios:

- A customer purchases a “bag of 100 coins” in your app and spends all 100 coins. The In-App Purchase is considered fully consumed.
- If your app has an exchange platform that has bartering, or if your app transferred an In-App Purchase from one account to another customer’s account, the In-App Purchase is considered fully consumed.

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## consumptionpercentageautorenewablesubscriptionerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ConsumptionPercentageAutoRenewableSubscriptionError
```

## See Also

- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## creating-api-keys-to-authorize-api-requests

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI), the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI](doc://com.apple.documentation/documentation/AdvancedCommerceAPI), and the [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI) require JSON Web Tokens (JWTs) to authorize each request you make to the API. You generate JWTs using a private API key that you download from App Store Connect. For information about generating the JWT using your private key, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests).

An API key has two parts: a public portion that Apple keeps, and a private key that you download. Use the private key to sign tokens that authorize the API to access or submit your data to the App Store.

> **IMPORTANT:** Store your private keys in a secure place. Don’t share your keys, don’t store keys in a code repository, and don’t include keys in client-side code. If you suspect a private key is compromised, immediately revoke the key in App Store Connect. See [doc://com.apple.documentation/documentation/AppStoreConnectAPI/revoking-api-keys](doc://com.apple.documentation/documentation/AppStoreConnectAPI/revoking-api-keys) for details.

Use the API key for the App Store Server API, the Advanced Commerce API, and the External Purchase Server API. You can’t use the key for other Apple services.

### 

To generate an API key to use with the App Store Server API, the Advanced Commerce API, and the External Purchase Server API, log in to [https://appstoreconnect.apple.com](https://appstoreconnect.apple.com) and complete the following steps:

1. On the homepage, click Users and Access.
2. Click the Integrations tab.
3. In the sidebar under Keys, click In-App Purchase.
4. Click Generate In-App Purchase Key. If you already have an Active In-App Purchase key generated, click the Add (+) icon to add more.
5. Enter a name for the key. The name is for your reference only and is not part of the key itself.
6. Click Generate.

After you generate an in-app purchase key, you cannot edit its name. If you need to make changes, revoke the key and generate a new one.

The new key’s name, key ID, a download link, and other information appear on the page.

### 

After generating your API key, App Store Connect gives you the opportunity to download the private half of the key. The private key is only available for download a single time.

1. Log in to [https://appstoreconnect.apple.com/](https://appstoreconnect.apple.com/).
2. On the homepage, click Users and Access.
3. Click the Integrations tab.
4. In the sidebar under Keys, click In-App Purchase.
5. Navigate to a key under the Active section, then click Download Key for the key you want to download.
6. In the dialog, click Download.

The download link appears only if you haven’t yet downloaded the private key. Apple doesn’t keep a copy of the private key. Store your private key in a secure place.

## See Also

- [simplifying-your-implementation-by-using-the-app-store-server-library](../com.apple.appstoreserverapi/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library.md)
- [generating-json-web-tokens-for-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
- [identifying-rate-limits](../com.apple.appstoreserverapi/AppStoreServerAPI/identifying-rate-limits.md)
- [app-store-server-api-changelog](../com.apple.appstoreserverapi/AppStoreServerAPI/app-store-server-api-changelog.md)

---


## currency

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string currency
```

## 

The currency property contains an ISO 4217 alpha-3 string that represents the currency of the price of the product.

> **IMPORTANT:** For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency) value to infer the storefront. Use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront) value in the transaction instead.

For more information on how you set prices, see [https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) and [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [price](../com.apple.appstoreserverapi/AppStoreServerAPI/price.md)

---


## customerConsented

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean customerConsented
```

## 

Set this field to `true` if the customer provided consent to send the App Store the consumption data related to their refund request, including all the data you provide in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest) or [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) request body. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

## See Also

- [consumptionPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionPercentage.md)
- [deliveryStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatus.md)
- [refundPreference](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreference.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)

---


## data-types

## Topics

### Environment

- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)

### Transaction identifiers

- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [transactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/transactionId.md)
- [webOrderLineItemId](../com.apple.appstoreserverapi/AppStoreServerAPI/webOrderLineItemId.md)

### App transaction identifier

- [appTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/appTransactionId.md)

### App information

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [originalApplicationVersion](../com.apple.appstoreserverapi/AppStoreServerAPI/originalApplicationVersion.md)
- [originalPlatform](../com.apple.appstoreserverapi/AppStoreServerAPI/originalPlatform.md)
- [preorderDate](../com.apple.appstoreserverapi/AppStoreServerAPI/preorderDate.md)

### Account information

- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)

### Product information

- [productId](../com.apple.appstoreserverapi/AppStoreServerAPI/productId.md)
- [type](../com.apple.appstoreserverapi/AppStoreServerAPI/type.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/subscriptionGroupIdentifier.md)
- [quantity](../com.apple.appstoreserverapi/AppStoreServerAPI/quantity.md)

### Product price and currency

- [price](../com.apple.appstoreserverapi/AppStoreServerAPI/price.md)
- [currency](../com.apple.appstoreserverapi/AppStoreServerAPI/currency.md)

### Storefront information

- [storefront](../com.apple.appstoreserverapi/AppStoreServerAPI/storefront.md)
- [storefrontId](../com.apple.appstoreserverapi/AppStoreServerAPI/storefrontId.md)

### Offers

- [eligibleWinBackOfferIds](../com.apple.appstoreserverapi/AppStoreServerAPI/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/offerPeriod.md)
- [offerType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerType.md)
- [offerDiscountType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerDiscountType.md)

### Product purchase dates

- [originalPurchaseDate](../com.apple.appstoreserverapi/AppStoreServerAPI/originalPurchaseDate.md)
- [purchaseDate](../com.apple.appstoreserverapi/AppStoreServerAPI/purchaseDate.md)
- [recentSubscriptionStartDate](../com.apple.appstoreserverapi/AppStoreServerAPI/recentSubscriptionStartDate.md)

### Billing status

- [isInBillingRetryPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/isInBillingRetryPeriod.md)
- [gracePeriodExpiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/gracePeriodExpiresDate.md)

### Subscription renewal and expiration

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

### Family Sharing

- [inAppOwnershipType](../com.apple.appstoreserverapi/AppStoreServerAPI/inAppOwnershipType.md)

### Price increase status

- [priceIncreaseStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/priceIncreaseStatus.md)

### Revocation

- [revocationDate](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationDate.md)
- [revocationReason](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationReason.md)
- [revocationPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationPercentage.md)
- [revocationType](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationType.md)

### Transaction reason

- [transactionReason](../com.apple.appstoreserverapi/AppStoreServerAPI/transactionReason.md)

### JSON Web Signature (JWS) date

- [signedDate](../com.apple.appstoreserverapi/AppStoreServerAPI/signedDate.md)
- [receiptCreationDate](../com.apple.appstoreserverapi/AppStoreServerAPI/receiptCreationDate.md)

### Advanced Commerce API data

- [advancedcommerce-datatypes](../com.apple.appstoreserverapi/AppStoreServerAPI/advancedcommerce-datatypes.md)

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)

---


## deliveryStatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string deliveryStatus
```

## 

Use these delivery status values in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest) request body.

> **NOTE:** If the delivery status isn’t `DELIVERED`, set the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage) to `0`; otherwise, the request fails with an error.

## See Also

- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [consumptionPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionPercentage.md)
- [refundPreference](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreference.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)

---


## deliverystatusv1

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 deliveryStatusV1
```

## 

Use these delivery status values in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) request body.

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## effectiveDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp effectiveDate
```

## See Also

- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [success](../com.apple.appstoreserverapi/AppStoreServerAPI/success.md)
- [webOrderLineItemId](../com.apple.appstoreserverapi/AppStoreServerAPI/webOrderLineItemId.md)

---


## eligiblewinbackofferids

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
[offerIdentifier] eligibleWinBackOfferIds
```

## 

Use this list to select an eligible win-back offer for a customer. The array contains strings that represent offer identifiers for win-back offers.  You provide the offer identifier in App Store Connect when you configure a win-back offer.

The App Store sets the order of the eligible win-back offer IDs for each customer, with the best offer first. The order takes into account the available offers you configure in App Store Connect for the customer’s most recent subscription in the subscription group. Subscriptions in a Billing Grace Period or billing retry state aren’t eligible for win-back offers.

Win-back offers have a direct link. App Store Connect generates and displays the direct link when you configure the win-back offer. Use the direct link to merchandise the win-back offer through your own channels. For more information, see [doc://com.apple.documentation/documentation/StoreKit/supporting-win-back-offers-in-your-app](doc://com.apple.documentation/documentation/StoreKit/supporting-win-back-offers-in-your-app).

This array appears in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload).

For information about configuring win-back offers in App Store Connect, see [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers).

## See Also

- [offerIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/offerPeriod.md)
- [offerType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerType.md)
- [offerDiscountType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerDiscountType.md)

---


## endDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp endDate
```

## 

The end date must be later than the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/startDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/startDate).

## See Also

- [startDate](../com.apple.appstoreserverapi/AppStoreServerAPI/startDate.md)
- [notificationType](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationType.md)
- [notificationSubtype](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationSubtype.md)
- [onlyFailures](../com.apple.appstoreserverapi/AppStoreServerAPI/onlyFailures.md)

---


## environment

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string environment
```

## 

You receive data from the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) for the sandbox environment when you send test requests to the endpoints using the sandbox base URL:

```javascript
https://api.storekit-sandbox.itunes.apple.com/
```

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)
- [revision](../com.apple.appstoreserverapi/AppStoreServerAPI/revision.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

---


## error-codes

## Topics

### Errors

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)
- [InvalidRequestIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRequestIdentifierError.md)
- [InvalidRequestRevisionError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRequestRevisionError.md)
- [InvalidRevokedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRevokedError.md)
- [InvalidStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStatusError.md)
- [InvalidStorefrontCountryCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStorefrontCountryCodeError.md)
- [InvalidTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionIdError.md)
- [OriginalTransactionIdNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/OriginalTransactionIdNotFoundError.md)
- [RateLimitExceededError](../com.apple.appstoreserverapi/AppStoreServerAPI/RateLimitExceededError.md)
- [StatusRequestNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/StatusRequestNotFoundError.md)
- [SubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/SubscriptionExtensionIneligibleError.md)
- [SubscriptionMaxExtensionError](../com.apple.appstoreserverapi/AppStoreServerAPI/SubscriptionMaxExtensionError.md)
- [TransactionIdIsNotOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/TransactionIdIsNotOriginalTransactionIdError.md)
- [TransactionIdNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TransactionIdNotFoundError.md)

### Errors to retry

- [AccountNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundRetryableError.md)
- [AppNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundRetryableError.md)
- [GeneralInternalRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalRetryableError.md)
- [OriginalTransactionIdNotFoundRetryableError](../com.apple.appstoreserverapi/AppStoreServerAPI/OriginalTransactionIdNotFoundRetryableError.md)

### Consumption request errors

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

### Notification test and history errors

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)
- [InvalidExcludeRevokedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExcludeRevokedError.md)

---


## expirationIntent

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 expirationIntent
```

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## expiresdate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp expiresDate
```

## 

The `expiresDate` is a static value that applies for each transaction. When the auto-renewable subscription renews, the App Store creates a new transaction with a new [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/expiresDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/expiresDate).

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## extend-a-subscription-renewal-date

## 

Use this endpoint to compensate your customers for temporary service outages, canceled events, or interruptions to live streamed events by extending the renewal date of their paid, active subscription. This endpoint acts on a single subscription for a transaction identifier that you specify.

To call this endpoint, provide the original transaction identifier of the subscription that experienced the service interruption. In the request body, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ExtendRenewalDateRequest), provide the extension duration, the reason code for the extension, and a unique [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier) for each extension request.

When this endpoint extends eligible purchased subscriptions that support Family Sharing, it automatically extends the family members’ subscriptions as well. However, the endpoint doesn’t support requests to extend a family member’s subscription directly.

A successful response with an `HTTP` `200` status code contains the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ExtendRenewalDateResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ExtendRenewalDateResponse) object. The response object includes the same unique request identifier you provide in the request, and information you need to determine whether the extension succeeds. For successful extensions, the new subscription expiration date is the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/effectiveDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/effectiveDate). All status codes other than `HTTP` `200` indicate that the request failed.

> **NOTE:** After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

After a successful renewal date extension, Apple sends an email to notify the customer of their updated subscription renewal date.

For more information about this and related endpoints, including subscription eligibility, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## extendByDays

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 extendByDays
```

## 

The number of days is a number from 1 to 90.

## See Also

- [extendReasonCode](../com.apple.appstoreserverapi/AppStoreServerAPI/extendReasonCode.md)
- [requestIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/requestIdentifier.md)

---


## extendReasonCode

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 extendReasonCode
```

## 

For more information about requesting subscription-renewal-date extensions, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [extendByDays](../com.apple.appstoreserverapi/AppStoreServerAPI/extendByDays.md)
- [requestIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/requestIdentifier.md)

---


## extending-the-renewal-date-for-auto-renewable-subscriptions

## 

If your service experiences a temporary outage, canceled event, or interruption to a live streamed event, you may choose to compensate your customers by extending the renewal date of their paid, active subscription. The App Store Server API provides two endpoints for requesting such extensions:

- [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) for an individual subscription
- [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) for all subscriptions based on a product identifier, optionally limited to a list of storefronts

You can move the renewal date for active auto-renewable subscriptions up to 90 days into the future if your service experiences an unexpected outage. To give you flexibility to resolve service issues or outages, you can extend the renewal date twice within a year (365 days) per customer.

> **NOTE:** After the subscription renewal extension goes into effect, there’s no way to reverse it. The extension period doesn’t count toward the one year of paid service when the App Store calculates the developer’s commission rate.

After a successful renewal date extension, Apple sends an email to notify the customer of their updated subscription renewal date.

### 

Only active auto-renewable subscriptions with at least one previously paid period are eligible to have a renewal date extension.

The following types of subscriptions aren’t eligible for renewal date extensions:

- Subscriptions in a free offer period
- Inactive subscriptions in a billing retry state
- Subscriptions in a billing grace period state with an expiration date in the past
- Subscriptions that have already received two renewal date extensions within the past 365 days
- Expired subscriptions

The App Store attempts to extend the renewal dates for eligible subscriptions only.

When the system extends eligible purchased subscriptions that support Family Sharing, it automatically extends the family members’ subscriptions as well. However, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint doesn’t support requests to extend a family member’s subscription directly.

### 

To request a renewal date extension for all eligible subscribers, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint. You indicate the subscription by its [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/productId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/productId). This endpoint is convenient for applying the renewal date extension to a large number of subscriptions with just one call. If a server outage affects some regions and not others, you can limit the request by storefront by including the optional `storefrontCountryCodes` property in the request body, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest).

To request a renewal date extension for a single subscriber, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint. You identify the subscription with an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId). Use this endpoint to retry a renewal date extension that fails with the other endpoint, as the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions#Retry-attempts-that-fail](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions#Retry-attempts-that-fail) section below describes.

### 

Requests to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint can take hours or days to complete, depending on the number of subscribers. The App Store server sends real-time notifications as it processes your request. The notifications inform you as each renewal date extension succeeds or fails, as well as when your request is complete.

To receive notifications, support [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) on your server. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).

The following table lists the notifications and their [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) and [doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype](doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype) values:

| Notification type | Subtype | Description |
| --- | --- | --- |
| `RENEWAL_EXTENDED` | (none) | The App Store extended the subscription renewal date for a specific subscription. |
| `RENEWAL_EXTENSION` | `FAILURE` | The subscription-renewal-date extension failed for a specific subscription. |
| `RENEWAL_EXTENSION` | `SUMMARY` | The request is complete. |

For more information about the contents of a notification payload, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload).

For requests to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint, [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications) sends a `RENEWAL_EXTENDED` notification when the request succeeds. The endpoint returns more information in its response body, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ExtendRenewalDateResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ExtendRenewalDateResponse).

### 

To check whether your request to [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) is complete, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoint. Complete requests include the final count of successful and failed renewal date extensions. If you don’t need this status on demand, use [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications) for status information instead, as the previous section describes.

### 

The App Store server sends real-time notifications as it processes your request to [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers). The notifications inform you each time an attempt to extend the renewal date succeeds or fails. You can retry the failed attempts by calling the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint with the failed subscription’s transaction identifier. Follow these steps:

1. Support [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) on your server. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).
2. Look for notifications with a [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) of `RENEWAL_EXTENSION` and [doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype](doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype) of `FAILURE`. The notification identifies a specific subscription that failed to receive a subscription-renewal-date extension.
3. Find the subscription’s transaction identifier in the notification’s payload, [doc://com.apple.documentation/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload). Specifically, use the `originalTransactionId` in the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload), which you get from the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransaction](doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransaction) of the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/data](doc://com.apple.documentation/documentation/AppStoreServerNotifications/data) object in the payload.
4. Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) using the `originalTransactionID`.

## See Also

- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## extendrenewaldaterequest

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ExtendRenewalDateRequest
```

## 

Use this object with the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint.

## Topics

### Request data types

- [extendByDays](../com.apple.appstoreserverapi/AppStoreServerAPI/extendByDays.md)
- [extendReasonCode](../com.apple.appstoreserverapi/AppStoreServerAPI/extendReasonCode.md)
- [requestIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/requestIdentifier.md)

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## extendrenewaldateresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object ExtendRenewalDateResponse
```

## 

This object is the response data for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint.

## Topics

### Response data types

- [effectiveDate](../com.apple.appstoreserverapi/AppStoreServerAPI/effectiveDate.md)
- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [success](../com.apple.appstoreserverapi/AppStoreServerAPI/success.md)
- [webOrderLineItemId](../com.apple.appstoreserverapi/AppStoreServerAPI/webOrderLineItemId.md)

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## failedCount

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 failedCount
```

## 

For information about retrying a renewal date extension when if fails, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [complete](../com.apple.appstoreserverapi/AppStoreServerAPI/complete.md)
- [completeDate](../com.apple.appstoreserverapi/AppStoreServerAPI/completeDate.md)
- [succeededCount](../com.apple.appstoreserverapi/AppStoreServerAPI/succeededCount.md)

---


## familytransactionnotsupportederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object FamilyTransactionNotSupportedError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## generalinternalerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object GeneralInternalError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## generating-json-web-tokens-for-api-requests

## 

JSON Web Token (JWT) is an open standard ([https://tools.ietf.org/html/rfc7519](https://tools.ietf.org/html/rfc7519)) that defines a way to securely transmit information. The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) and [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI) require a JWT to authorize each request you make to the API. You create the token, signing it with the private key you downloaded from App Store Connect. For more information about creating keys, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests).

To generate a signed JWT:

1. Create the JWT header.
2. Create the JWT payload.
3. Sign the JWT.

Include the signed JWT in the authorization header of each API request. Generate a new signed JWT for each new request.

> **TIP:** The App Store Server Library provides an API client and creates JWTs for use with the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI). For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

### 

To create a JWT to communicate with the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) or [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI), use the following fields and values in the header:

| Header Field | Value |
| --- | --- |
| `alg` - Encryption Algorithm | `ES256`   All JWTs must be signed with ES256 encryption |
| `kid` - Key ID | Your private key ID from App Store Connect (Ex: `2X9R4HXF34`) |
| `typ` - Token Type | `JWT` |

To get your key ID, copy it from App Store Connect by logging in to [https://appstoreconnect.apple.com/](https://appstoreconnect.apple.com/), then:

1. Select Users and Access, then select the Keys tab.
2. The key IDs appear in a column under the Active heading. Hover the cursor next to a key ID to display the Copy Key ID link.
3. Click Copy Key ID.

If you have more than one API key, copy the key ID of the private key that you use to sign the JWT.

Here’s an example of a JWT header:

```javascript
{
  "alg": "ES256",
  "kid": "2X9R4HXF34",
  "typ": "JWT"
}
```

### 

The JWT payload contains information specific to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) and [doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI](doc://com.apple.documentation/documentation/ExternalPurchaseServerAPI), such as issuer ID and expiration time. Use the following fields — also known as JWT claims — to include these values in the JWT payload:

| **Payload Field** | **Value** |
| --- | --- |
| `iss` - Issuer | Your issuer ID from the Keys page in App Store Connect (Ex: “`57246542-96fe-1a63-e053-0824d011072a"`) |
| `iat` - Issued At | The time at which you issue the token, in UNIX time, in seconds (Ex: `1623085200`) |
| `exp` - Expiration Time | The token’s expiration time, in UNIX time, in seconds. Tokens that expire more than 60 minutes after the time in `iat` are not valid (Ex: `1623086400`) |
| `aud` - Audience | `appstoreconnect-v1` |
| `bid` - Bundle ID | Your app’s bundle ID (Ex: `“com.example.testbundleid”)` |

To get your issuer ID, log in to [https://appstoreconnect.apple.com/](https://appstoreconnect.apple.com/), then:

1. Select Users and Access, then select the Keys tab.
2. The issuer ID appears near the top of the page. To copy the issuer ID, click Copy next to the ID.

Here’s an example of a JWT payload:

```javascript
{
  "iss": "57246542-96fe-1a63e053-0824d011072a",
  "iat": 1623085200,
  "exp": 1623086400,
  "aud": "appstoreconnect-v1",
  "bid": "com.example.testbundleid"
}
```

Note that the JWT is valid for up to one hour after the time you indicate in the `iat` field, or it expires sooner if you set the `exp` field for an earlier time.

### 

Use the private key associated with the key ID you specified in the header to sign the token using ES256 encryption.

There are a variety of open source libraries available online for creating and signing JWT tokens. See [https://jwt.io/](https://jwt.io/) for more information.  For calls to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI), consider using the App Store Server Library to create the JWTs instead. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

### 

After you create and sign the JWT, provide it in the request’s authorization header as a bearer token.

The following example for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) shows a `curl` command using a bearer token. Replace the text `[signed token]` with the value of the signed JWT itself. Replace `{transactionId}` with a transaction identifier of your customer.

```other
curl -v -H 'Authorization: Bearer [signed token]' 
"https://api.storekit.itunes.apple.com/inApps/v1/subscriptions/{transactionId}"
```

## See Also

- [simplifying-your-implementation-by-using-the-app-store-server-library](../com.apple.appstoreserverapi/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library.md)
- [creating-api-keys-to-authorize-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
- [identifying-rate-limits](../com.apple.appstoreserverapi/AppStoreServerAPI/identifying-rate-limits.md)
- [app-store-server-api-changelog](../com.apple.appstoreserverapi/AppStoreServerAPI/app-store-server-api-changelog.md)

---


## get-app-transaction-info

## 

Use this endpoint to get the app transaction information for a customer of your app. You can provide any transaction ID that belongs to the customer to get their app transaction information.

App transaction information represents the customer’s purchase of the app, cryptographically signed by the App Store. The App Store generates a single, globally unique [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appTransactionId) for each Apple Account that downloads your app and for each family group member for apps that support Family Sharing. The `appTransactionId` value remains the same for the same Apple Account and app if the customer redownloads the app on any device, receives a refund, repurchases the app, or changes the storefront. For apps that support Family Sharing, the `appTransactionId` is unique for each family group member.

App transaction information includes details about the app the customer purchased, such as its bundleID, original version, original purchase date, and more. You can also get app transaction information in your app from StoreKit, using [doc://com.apple.documentation/documentation/StoreKit/AppTransaction](doc://com.apple.documentation/documentation/StoreKit/AppTransaction).

## See Also

- [AppTransactionInfoResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionInfoResponse.md)

---


## get-test-notification-status

## 

Call this endpoint using the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status/testNotificationToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status/testNotificationToken) you receive when you call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification). You can check the status using the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status/testNotificationToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status/testNotificationToken) for up to six months. Use the information in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/CheckTestNotificationResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/CheckTestNotificationResponse) to troubleshoot your server if it’s unable to receive App Store Server Notifications successfully.

## See Also

- [Request-a-Test-Notification](../com.apple.appstoreserverapi/AppStoreServerAPI/Request-a-Test-Notification.md)
- [SendTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/SendTestNotificationResponse.md)
- [CheckTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/CheckTestNotificationResponse.md)

---


## get-transaction-history-v1

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) endpoint returns results for the following product types:

- Auto-renewable subscriptions
- Non-renewing subscriptions
- Non-consumable in-app purchases
- Consumable in-app purchases if the transaction is refunded or revoked, or if the app hasn’t finished processing the transaction. The results don’t include consumable in-app purchases that the app marks as finished. For more information about finishing transactions, see [doc://com.apple.documentation/documentation/StoreKit/Transaction/finish()](doc://com.apple.documentation/documentation/StoreKit/Transaction/finish()) and [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)).

> **NOTE:** Use [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) instead to get all the product types, including consumable in-app purchases in the finished state.

You can customize your request by including query parameters that filter the transaction history. The query parameters limit the scope of the request by dates, product IDs, product types, and subscription group identifiers. You can also exclude revoked or nonrevoked transactions, and limit the transactions by in-app ownership type. If you provide multiple filters in the query, the transactions that return match all the filters.

You can also specify a sort order. The App Store sorts the transactions based on their recently modified dates. Use a `DESCENDING` order to get the most recent transactions first. The App Store updates the recently modified date if the customer upgrades a subscription or the App Store revokes an in-app purchase. If a transaction updates while you’re receiving transaction history and the response is sorted in `ASCENDING` order, you may receive the transaction again with updated data.

The `productId`, `productType`, and `subscriptionGroupIdentifier` query parameters allow you to specify multiple values. To specify more than one value for a query parameter, include it in the request multiple times. For example, to filter the transaction history by non-consumable and auto-renewable product types, include the following within your request:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/history/{transactionId}?productType=NON_CONSUMABLE&productType=AUTO_RENEWABLE
```

When you specify multiple values for a single query parameter, the response contains transactions that match any of the values.

> **NOTE:** If you use optional query parameters, be sure to use the same query parameters on subsequent requests that include the `revision` parameter.

To request a full transaction history in ascending order for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/history/{transactionId}
```

For subsequent requests, include the `revision` token from the previous [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse).

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/history/{transactionId}?revision={revision}
```

## See Also

- [Get-Refund-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History-V1.md)
- [Send-Consumption-Information-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Send-Consumption-Information-V1.md)
- [ConsumptionRequestV1](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequestV1.md)
- [RefundLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundLookupResponse.md)

---


## get-transaction-history

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint returns results for all in-app purchase product types: auto-renewable subscriptions, non-renewing subscriptions, non-consumable, and consumable. The result returns transactions in any state, including transactions that are refunded or revoked, and transactions that the app has or hasn’t marked as finished.

You can customize your request by including query parameters that filter the transaction history. The query parameters limit the scope of the request by dates, product IDs, product types, and subscription group identifiers. You can also exclude revoked or nonrevoked transactions, and limit the transactions by in-app ownership type. If you provide multiple filters in the query, the transactions that return match all the filters.

You can also specify a sort order. The App Store sorts the transactions based on their recently modified dates. Use a `DESCENDING` order to get the most recent transactions first. The App Store updates the recently modified date if the customer upgrades a subscription or the App Store revokes an in-app purchase. If a transaction updates while you’re receiving transaction history and the response is sorted in `ASCENDING` order, you may receive the transaction again with updated data.

The `productId`, `productType`, and `subscriptionGroupIdentifier` query parameters allow you to specify multiple values. To specify more than one value for a query parameter, include it in the request multiple times. For example, to filter the transaction history by non-consumable and auto-renewable product types, include the following within your request:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/history/{transactionId}?productType=NON_CONSUMABLE&productType=AUTO_RENEWABLE
```

When you specify multiple values for a single query parameter, the response contains transactions that match any of the values.

> **NOTE:** If you use optional query parameters, be sure to use the same query parameters on subsequent requests that include the `revision` parameter.

To request a full transaction history in ascending order for your app, start by calling the endpoint without any query parameters, as follows:

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/history/{transactionId}} 
```

For subsequent requests, include the `revision` token from the previous [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse).

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v2/history/{transactionId}?revision={revision}
```

## See Also

- [HistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/HistoryResponse.md)

---


## get-transaction-info

## 

Use this endpoint to get transaction information for any transaction identifier, including original transaction identifiers.  This endpoint supports all in-app purchase types, including consumable, non-consumable, non-renewing subscriptions, and auto-renewable subscriptions. It also supports transactions that your app marked as finished using [doc://com.apple.documentation/documentation/StoreKit/Transaction/finish()](doc://com.apple.documentation/documentation/StoreKit/Transaction/finish()) or [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)) in StoreKit.

## See Also

- [TransactionInfoResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/TransactionInfoResponse.md)

---


## gracePeriodExpiresDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp gracePeriodExpiresDate
```

## 

For more information about billing grace periods, see [https://help.apple.com/app-store-connect/#/dev58bda3212](https://help.apple.com/app-store-connect/#/dev58bda3212).

## See Also

- [isInBillingRetryPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/isInBillingRetryPeriod.md)

---


## hasMore

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean hasMore
```

## 

This value is `true` if the App Store has more transactions for the customer. Call the endpoint again, including the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revision) or [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/paginationToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/paginationToken) query parameter, to get the next set of transactions.

If this value is `false`, there aren’t any additional transactions.

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore) value appears in responses to endpoints that provide paginated results, such as [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/NotificationHistoryResponse), [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse), and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse).

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [revision](../com.apple.appstoreserverapi/AppStoreServerAPI/revision.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

---


## historyresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object HistoryResponse
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint returns the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse). This response contains results for all in-app purchase product types: auto-renewable subscriptions, non-renewing subscriptions, non-consumables, and consumables. The result includes transactions in any state, including transactions that are refunded or revoked, and transactions that the app has or hasn’t marked as finished.

The history response returns a maximum of 20 transactions per response. If your customer has more than 20 in-app transactions, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse/hasMore) value is `true`. Each response includes a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse/revision) value. Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) again with the `revision` token in the query to receive the next set of transactions; use the same query parameters for each subsequent call that includes `revision`. When the App Store has no more transactions to send, the `hasMore` value is `false`.

If a customer upgrades a subscription or the App Store revokes an in-app purchase while you’re receiving transaction history, the App Store updates the relevant transaction. If the response is sorted in `ASCENDING` order, you receive the transaction again, with updated data.

> **NOTE:** The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) endpoint also returns the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/HistoryResponse), however, it doesn’t include consumable in-app purchases that the app has marked as finished. Use [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) instead.

## Topics

### Response data types

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)
- [revision](../com.apple.appstoreserverapi/AppStoreServerAPI/revision.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

## See Also

- [Get-Transaction-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History.md)

---


## identifying-rate-limits

## 

The App Store Server API limits the number of requests that you can submit to each endpoint within a specified timespan. The request limits apply per app.

The following table lists the rate limits for each endpoint in the production environment, expressed in requests per second. The system enforces rate limits on an hourly basis.

| Endpoint | Rate limit (per second) |
| --- | --- |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-Info) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History-V1) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) | 50 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) | 20 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token) | 20 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID) | 10 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History) | 10 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History-V1) | 10 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) | 1 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification) | 1 |
| [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status) | 1 |

The rate limits in the sandbox environment are 10% of the limits in the table above.

The App Store server may make adjustments to reduce or increase these rate limits as needed at any time.

### 

If you exceed a per-hour limit, the API rejects the request with an `HTTP` `429` response, with a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError) in the body.  Consider the following as you integrate the API:

- If you periodically call the API, throttle your requests to avoid exceeding the per-hour limit for an endpoint.
- Manage the `HTTP` `429` [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RateLimitExceededError) in your error-handling process. For example, log the failure and queue the job to process it again at a later time.
- Check the `Retry-After` header if you receive the `HTTP` `429` error. This header contains a UNIX time, in milliseconds, that informs you when you can next send a request.

## See Also

- [simplifying-your-implementation-by-using-the-app-store-server-library](../com.apple.appstoreserverapi/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library.md)
- [creating-api-keys-to-authorize-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
- [generating-json-web-tokens-for-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
- [app-store-server-api-changelog](../com.apple.appstoreserverapi/AppStoreServerAPI/app-store-server-api-changelog.md)

---


## inAppOwnershipType

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string inAppOwnershipType
```

---


## invalidaccounttenureerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidAccountTenureError
```

## 

For more information about `accountTenure` values in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/accountTenure](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/accountTenure).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invalidappaccounttokenerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidAppAccountTokenError
```

## 

For more information about the `appAccountToken` field in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/appAccountToken).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invalidappaccounttokenuuiderror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidAppAccountTokenUUIDError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## invalidappidentifiererror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidAppIdentifierError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## invalidconsumptionstatuserror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidConsumptionStatusError
```

## 

For more information about the `consumptionStatus` field in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionStatus).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invalidcustomerconsentederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidCustomerConsentedError
```

## 

If the `customerConsented` field in [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest) or [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) is any value other than `true`, the App Store server rejects the request. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invaliddeliverystatuserror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidDeliveryStatusError
```

## 

For valid delivery status values, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/deliveryStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/deliveryStatus) for [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest), or [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/deliveryStatusV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/deliveryStatusV1) for [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invalidemptystorefrontcountrycodelisterror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidEmptyStorefrontCountryCodeListError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint. If your request applies to all storefronts, omit the `storefrontCountryCodes` list from the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest) object.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## invalidextendbydayserror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidExtendByDaysError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extendByDays](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extendByDays) you provide in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoints.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## invalidextendreasoncodeerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidExtendReasonCodeError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extendReasonCode](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extendReasonCode) you provide in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoints.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)
- [InvalidRefundPreferenceError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidRefundPreferenceError.md)

---


## invalidinappownershiptypeerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidInAppOwnershipTypeError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## invalidlifetimedollarspurchasederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidLifetimeDollarsPurchasedError
```

## 

For valid `lifetimeDollarsPurchased` values in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1), see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/lifetimeDollarsPurchased](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/lifetimeDollarsPurchased).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invalidpaginationtokenerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidPaginationTokenError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## invalidproductiderror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidProductIdError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## invalidrefundpreferenceerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidRefundPreferenceError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreference](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreference) value you provide in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest), or the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreferenceV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/refundPreferenceV1) value in a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1).

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## invalidrevokederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidRevokedError
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint returns this error if you provide an invalid value for the `revoked` query parameter.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## invalidsamplecontentprovidederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidSampleContentProvidedError
```

## 

See [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sampleContentProvided](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sampleContentProvided) for valid values.

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## invalidsorterror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidSortError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## invalidstartdateerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidStartDateError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## invalidstatuserror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidStatusError
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-All-Subscription-Statuses) endpoint returns this error if you provide an invalid `status` query parameter.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## invalidtestnotificationtokenerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidTestNotificationTokenError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## invalidtransactioniderror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidTransactionIdError
```

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## invalidtransactionnotconsumableerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object InvalidTransactionNotConsumableError
```

## 

The system no longer sends this error.

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [UndeliveredConsumptionPercentageNonZeroError](../com.apple.appstoreserverapi/AppStoreServerAPI/UndeliveredConsumptionPercentageNonZeroError.md)

---


## isUpgraded

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean isUpgraded
```

## 

If `isUpgraded` is `true`, the customer has upgraded the subscription represented by this transaction to another subscription. This value appears in the transaction only when it’s `true`. To determine the service that the customer is entitled to, look for another transaction that has a subscription with a higher level of service.

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## isinbillingretryperiod

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean isInBillingRetryPeriod
```

## See Also

- [gracePeriodExpiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/gracePeriodExpiresDate.md)

---


## jwsapptransaction

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string JWSAppTransaction
```

## 

The `JWSAppTransaction` type is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the transaction information, signed by the App Store according to the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

- To read the transaction information, Base64URL-decode the payload. Use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload) object to read the payload information.
- To read the header, decode it and use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader) object to access the information. Use the information in the header to verify the signature.

### 

To verify a `JWSAppTransaction` on your server, consider implementing the verification using the App Store Server Library function `verifyAndDecodeAppTransaction`. The library provides this function in each language the library supports. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## jwsapptransactiondecodedpayload

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object JWSAppTransactionDecodedPayload
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-App-Transaction-Info) endpoint returns a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransaction](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransaction), which you decode to get `JWSAppTransactionDecodedPayload`.

You can also get app transaction information in your app from StoreKit, using [doc://com.apple.documentation/documentation/StoreKit/AppTransaction](doc://com.apple.documentation/documentation/StoreKit/AppTransaction).

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## jwsrenewalinfo

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string JWSRenewalInfo
```

## 

The `JWSRenewalInfo` type is a string of three Base64 URL-encoded components, separated by a period, containing subscription renewal information signed by the App Store. The App Store signs the string according to the JSON Web Signature (JWS) [https://datatracker.ietf.org/doc/html/rfc7515](https://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components in the string are a header, a payload, and a signature.

- To read the subscription renewal information, decode the payload. Use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) object to read the payload information.
- To read the header, decode it and use a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSDecodedHeader) object to access the information. Use the information in the header to verify the signature.

## See Also

- [JWSDecodedHeader](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSDecodedHeader.md)
- [JWSAppTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransaction.md)
- [JWSAppTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSAppTransactionDecodedPayload.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)
- [JWSTransactionDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransactionDecodedPayload.md)
- [JWSRenewalInfoDecodedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfoDecodedPayload.md)
- [data-types](../com.apple.appstoreserverapi/AppStoreServerAPI/data-types.md)

---


## lastTransactionsItem

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object lastTransactionsItem
```

## Topics

### Data Types

- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)
- [JWSRenewalInfo](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSRenewalInfo.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

## See Also

- [subscriptionGroupIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/SubscriptionGroupIdentifierItem/subscriptionGroupIdentifier.md)

---


## lifetimeDollarsPurchased

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 lifetimeDollarsPurchased
```

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## lifetimeDollarsRefunded

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 lifetimeDollarsRefunded
```

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## look-up-order-id

## 

> **IMPORTANT:** This endpoint isn’t available in the sandbox environment.

Call this endpoint to identify and validate a customer’s in-app purchases, based on their order ID.

When a customer contacts you for support, ask for their order ID and use that value to call this endpoint. Customers can retrieve their order IDs from their purchase history on the App Store; for more information, see [https://support.apple.com/en-gb/HT204088](https://support.apple.com/en-gb/HT204088). The App Store also sends customers an email receipt with an order ID each time they make in-app purchases.

A successful response with an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/OrderLookupStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/OrderLookupStatus) value of `0` contains an array of one or more signed transactions for the in-app purchase based on the order ID. Use the decoded transaction, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload), to identify information such as the `productId` and `purchaseDate` that you can use to provide customer support.

A response with an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/OrderLookupStatus](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/OrderLookupStatus) value of `1` doesn’t contain a signed transactions array.

The App Store Server API returns information based on the customer’s in-app purchase history regardless of whether the customer installed, removed, or reinstalled the app on their devices.

## Topics

### Request data types

- [orderId](../com.apple.appstoreserverapi/AppStoreServerAPI/orderId.md)

## See Also

- [orderId](../com.apple.appstoreserverapi/AppStoreServerAPI/orderId.md)
- [OrderLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/OrderLookupResponse.md)

---


## massextendrenewaldaterequest

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object MassExtendRenewalDateRequest
```

## 

This request body applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint.

The `requestIdentifier` uniquely identifies this request. Use the same `requestIdentifier` in the following APIs :

- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoint
- The [doc://com.apple.documentation/documentation/AppStoreServerNotifications/summary](doc://com.apple.documentation/documentation/AppStoreServerNotifications/summary) object in [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications).

For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## Topics

### Data types

- [extendByDays](../com.apple.appstoreserverapi/AppStoreServerAPI/extendByDays.md)
- [extendReasonCode](../com.apple.appstoreserverapi/AppStoreServerAPI/extendReasonCode.md)
- [productId](../com.apple.AppStoreServerNotifications/productId.md)
- [requestIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/requestIdentifier.md)
- [storefrontCountryCode](../com.apple.appstoreserverapi/AppStoreServerAPI/storefrontCountryCode.md)
- [storefrontCountryCodes](../com.apple.appstoreserverapi/AppStoreServerAPI/storefrontCountryCodes.md)

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## massextendrenewaldateresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object MassExtendRenewalDateResponse
```

## 

The App Store server returns this response when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint. Because the endpoint runs asynchronously, this response means the App Store received your request and is processing it. The request may take multiple hours or days to complete, depending on the number of subscribers.

As the App Store server processes your request, it sends notifications ([doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2)) in near real-time to report on each subscription it processes. Look for notifications with the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) of `RENEWAL_EXTENSION` and `RENEWAL_EXTENDED`. The server sends a `RENEWAL_EXTENSION` notification with a [doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype](doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype) of `SUCCESS` when it completes the request.

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoint reports on whether your request is complete. For completed requests, it also reports the count of successful and failed subscription-renewal-date extensions.

For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateStatusResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateStatusResponse.md)

---


## massextendrenewaldatestatusresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object MassExtendRenewalDateStatusResponse
```

## 

The App Store server sends this response when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions) endpoint. Your request to [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) is complete when the value of the `complete` field is `TRUE`. Otherwise, the request is still in progress.

The App Store server also sends real-time notifications as it’s processing the subscription-renewal-date extension, including notifications with [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) values of `RENEWAL_EXTENSION` and `RENEWAL_EXTENDED`. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications). For more information about extending subscription renewal dates, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## Topics

### Data types

- [complete](../com.apple.appstoreserverapi/AppStoreServerAPI/complete.md)
- [completeDate](../com.apple.appstoreserverapi/AppStoreServerAPI/completeDate.md)
- [failedCount](../com.apple.appstoreserverapi/AppStoreServerAPI/failedCount.md)
- [succeededCount](../com.apple.appstoreserverapi/AppStoreServerAPI/succeededCount.md)

## See Also

- [extending-the-renewal-date-for-auto-renewable-subscriptions](../com.apple.appstoreserverapi/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions.md)
- [Extend-a-Subscription-Renewal-Date](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date.md)
- [Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](../com.apple.appstoreserverapi/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers.md)
- [Get-Status-of-Subscription-Renewal-Date-Extensions](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Status-of-Subscription-Renewal-Date-Extensions.md)
- [ExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateRequest.md)
- [ExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/ExtendRenewalDateResponse.md)
- [MassExtendRenewalDateRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateRequest.md)
- [MassExtendRenewalDateResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/MassExtendRenewalDateResponse.md)

---


## notificationType

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string notificationType
```

## 

For the list of notification types available in [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications) version 2, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType).

## See Also

- [startDate](../com.apple.appstoreserverapi/AppStoreServerAPI/startDate.md)
- [endDate](../com.apple.appstoreserverapi/AppStoreServerAPI/endDate.md)
- [notificationSubtype](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationSubtype.md)
- [onlyFailures](../com.apple.appstoreserverapi/AppStoreServerAPI/onlyFailures.md)

---


## notificationhistoryresponseitem

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object notificationHistoryResponseItem
```

## Topics

### Data types

- [sendAttemptResult](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptResult.md)
- [sendAttemptItem](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptItem.md)
- [signedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/signedPayload.md)

## See Also

- [Get-Notification-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Notification-History.md)
- [NotificationHistoryRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryRequest.md)
- [NotificationHistoryResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/NotificationHistoryResponse.md)

---


## notificationsubtype

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string notificationSubtype
```

## 

For the list of notification subtypes available in [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications), see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype](doc://com.apple.documentation/documentation/AppStoreServerNotifications/subtype).

## See Also

- [startDate](../com.apple.appstoreserverapi/AppStoreServerAPI/startDate.md)
- [endDate](../com.apple.appstoreserverapi/AppStoreServerAPI/endDate.md)
- [notificationType](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationType.md)
- [onlyFailures](../com.apple.appstoreserverapi/AppStoreServerAPI/onlyFailures.md)

---


## offerType

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 offerType
```

## 

All offer types, except offer type `1`, have an [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerIdentifier](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerIdentifier).

You set up offers in App Store Connect. For more information on subscription offers, see [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions), [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions), [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes), and [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers). For more information on offer codes, see [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases).

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreserverapi/AppStoreServerAPI/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/offerPeriod.md)
- [offerDiscountType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerDiscountType.md)

---


## offerdiscounttype

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string offerDiscountType
```

## 

You set up subscription offers and determine the payment mode when you configure subscriptions in App Store Connect. For more information about the free trial, pay as you go, and pay up front payment modes, see [https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability](https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability).

For more information on subscription offers, see [https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreserverapi/AppStoreServerAPI/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/offerIdentifier.md)
- [offerPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/offerPeriod.md)
- [offerType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerType.md)

---


## offeridentifier

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string offerIdentifier
```

## 

The `offerIdentifier` is a string that you provide in App Store Connect when you set up a subscription offer. All offer types ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerType)) have offer identifiers, except for introductory offers.

For more information about subscription offers, see [https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers). For information about configuring the various types of subscription offers in App Store Connect, see:

- [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/)
- [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions)
- [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions)
- [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers)

## See Also

- [eligibleWinBackOfferIds](../com.apple.appstoreserverapi/AppStoreServerAPI/eligibleWinBackOfferIds.md)
- [offerPeriod](../com.apple.appstoreserverapi/AppStoreServerAPI/offerPeriod.md)
- [offerType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerType.md)
- [offerDiscountType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerDiscountType.md)

---


## offerperiod

## Declaration

**Platforms:** Unsupported OS: App Store Server API

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

- [eligibleWinBackOfferIds](../com.apple.appstoreserverapi/AppStoreServerAPI/eligibleWinBackOfferIds.md)
- [offerIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/offerIdentifier.md)
- [offerType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerType.md)
- [offerDiscountType](../com.apple.appstoreserverapi/AppStoreServerAPI/offerDiscountType.md)

---


## onlyfailures

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean onlyFailures
```

## 

A value of `true` indicates that you want to receive just the App Store server notifications that failed to reach your server, including those that the App Store server is currently retrying.

## See Also

- [startDate](../com.apple.appstoreserverapi/AppStoreServerAPI/startDate.md)
- [endDate](../com.apple.appstoreserverapi/AppStoreServerAPI/endDate.md)
- [notificationType](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationType.md)
- [notificationSubtype](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationSubtype.md)

---


## orderId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string orderId
```

## 

When customers make one or more in-app purchases in your app, the App Store emails them a receipt. The receipt contains an order ID. Use this order ID to call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID). Customers can also retrieve their order IDs from their purchase history on the App Store; for more information, see [https://support.apple.com/en-gb/HT204088](https://support.apple.com/en-gb/HT204088).

## See Also

- [Look-Up-Order-ID](../com.apple.appstoreserverapi/AppStoreServerAPI/Look-Up-Order-ID.md)
- [OrderLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/OrderLookupResponse.md)

---


## orderlookupresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object OrderLookupResponse
```

## 

The order lookup response contains information about the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/orderId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/orderId) you specify when you call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Look-Up-Order-ID).

If the `orderId` that you provide in the request is invalid, the response doesn’t include the `signedTransactions` array. If the `orderId` is valid, expect at least one transaction in the `signedTransactions` array.

## Topics

### Response data types

- [OrderLookupStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/OrderLookupStatus.md)

## See Also

- [Look-Up-Order-ID](../com.apple.appstoreserverapi/AppStoreServerAPI/Look-Up-Order-ID.md)
- [orderId](../com.apple.appstoreserverapi/AppStoreServerAPI/orderId.md)

---


## orderlookupstatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 OrderLookupStatus
```

---


## originalPlatform

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string originalPlatform
```

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [originalApplicationVersion](../com.apple.appstoreserverapi/AppStoreServerAPI/originalApplicationVersion.md)
- [preorderDate](../com.apple.appstoreserverapi/AppStoreServerAPI/preorderDate.md)

---


## originalPurchaseDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp originalPurchaseDate
```

## 

The original purchase date is in UNIX time, in milliseconds.

## See Also

- [purchaseDate](../com.apple.appstoreserverapi/AppStoreServerAPI/purchaseDate.md)
- [recentSubscriptionStartDate](../com.apple.appstoreserverapi/AppStoreServerAPI/recentSubscriptionStartDate.md)

---


## originalTransactionId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string originalTransactionId
```

## 

The App Store generates an original transaction identifier when a customer makes a successful in-app purchase. Most App Store Server API endpoints accept an `originalTransactionId`.

There are several ways to obtain this value: from your app after a user makes a successful in-app purchase, from transaction information provided in [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications), or from [doc://com.apple.documentation/documentation/AppStoreReceipts](doc://com.apple.documentation/documentation/AppStoreReceipts) for apps that use the [doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase).

To get the original transaction identifier from your app, use the [doc://com.apple.documentation/documentation/StoreKit/Transaction/originalID](doc://com.apple.documentation/documentation/StoreKit/Transaction/originalID) property of the [doc://com.apple.documentation/documentation/StoreKit/Transaction](doc://com.apple.documentation/documentation/StoreKit/Transaction) object that represents the in-app purchase.

If you’ve enabled [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications), your server receives notifications for in-app purchase events that include the transaction information with the original transaction identifier. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/responseBodyV2DecodedPayload).

If your app uses the [doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase), the original transaction identifier is the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier) property in the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction) object. For restored purchases, the original transaction identifier is found in the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier) of the [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/original](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/original) property. If you verify receipts using [doc://com.apple.documentation/documentation/AppStoreReceipts/Verify-Receipt](doc://com.apple.documentation/documentation/AppStoreReceipts/Verify-Receipt), the original transaction identifier is the [doc://com.apple.documentation/documentation/AppStoreReceipts/original_transaction_id](doc://com.apple.documentation/documentation/AppStoreReceipts/original_transaction_id) value.

Use the value of the original transaction identifier that you get from your app, a notification, or a receipt as the value for [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId) when you send requests to the App Store Server API.

> **TIP:** If you maintain a database to manage your subscribers, save the original transaction identifier to uniquely identify auto-renewable subscriptions.

## See Also

- [effectiveDate](../com.apple.appstoreserverapi/AppStoreServerAPI/effectiveDate.md)
- [success](../com.apple.appstoreserverapi/AppStoreServerAPI/success.md)
- [webOrderLineItemId](../com.apple.appstoreserverapi/AppStoreServerAPI/webOrderLineItemId.md)

---


## originalapplicationversion

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string originalApplicationVersion
```

## 

Use this value to determine which app version the customer first purchased or downloaded. This value remains constant and doesn’t change when the customer upgrades the app.

The string value contains the original value of the [doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString](doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/CFBundleShortVersionString) for apps running in macOS, and the original value of the [doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/CFBundleVersion](doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/CFBundleVersion) for apps running on all other platforms.

In the sandbox testing environment, the `originalApplicationVersion` value is always 1.0.

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [originalPlatform](../com.apple.appstoreserverapi/AppStoreServerAPI/originalPlatform.md)
- [preorderDate](../com.apple.appstoreserverapi/AppStoreServerAPI/preorderDate.md)

---


## paginationToken

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string paginationToken
```

## 

A token you use in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) endpoint to ask for the next set of up to 20 notification history entries. All responses include a `paginationToken`.

## See Also

- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)

---


## platform

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 platform
```

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## playTime

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 playTime
```

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## preorderDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp preorderDate
```

## 

For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload).

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [originalApplicationVersion](../com.apple.appstoreserverapi/AppStoreServerAPI/originalApplicationVersion.md)
- [originalPlatform](../com.apple.appstoreserverapi/AppStoreServerAPI/originalPlatform.md)

---


## price

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 price
```

## 

This value represents the price, in milliunits of the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/currency](doc://com.apple.documentation/documentation/AppStoreServerNotifications/currency), of the In-App Purchase that the system records in the transaction. One unit of the currency equals 1000 milliunits.

The `price` value reflects all of the following:

- The price you configured in App Store Connect, which the system records on the purchase date ([doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/purchaseDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/purchaseDate)).
- The discount from a subscription offer in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerIdentifier](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/offerIdentifier), if the transaction includes an offer.
- The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/quantity](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/quantity) of a consumable in-app purchase. The price value shows the total amount of the transaction for the quantity the customer purchased.

The following table shows some examples of the `price` and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency) parameters based on sample prices you might configure in App Store Connect:

| Configured price in App Store Connect | `price` parameter | `currency` parameter |
| --- | --- | --- |
| $1.99 (U.S. dollar) | 1990 | USD |
| KRW 3300 (South Korean won) | 3300000 | KRW |
| JPY 300 (Japanese yen) | 300000 | JPY |

To determine the storefront, use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront) value in the transaction. Don’t use the `currency` value to infer the storefront.

> **IMPORTANT:** For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

For more information on how you set prices, see [https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price](https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) and [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [currency](../com.apple.appstoreserverapi/AppStoreServerAPI/currency.md)

---


## priceincreasestatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 priceIncreaseStatus
```

---


## productId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string productId
```

## 

You define product IDs in App Store Connect. Product IDs are unique within your app.

## See Also

- [type](../com.apple.appstoreserverapi/AppStoreServerAPI/type.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/subscriptionGroupIdentifier.md)
- [quantity](../com.apple.appstoreserverapi/AppStoreServerAPI/quantity.md)

---


## purchaseDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp purchaseDate
```

## 

The purchase date is in UNIX time, in milliseconds.

## See Also

- [originalPurchaseDate](../com.apple.appstoreserverapi/AppStoreServerAPI/originalPurchaseDate.md)
- [recentSubscriptionStartDate](../com.apple.appstoreserverapi/AppStoreServerAPI/recentSubscriptionStartDate.md)

---


## quantity

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 quantity
```

## See Also

- [productId](../com.apple.appstoreserverapi/AppStoreServerAPI/productId.md)
- [type](../com.apple.appstoreserverapi/AppStoreServerAPI/type.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/subscriptionGroupIdentifier.md)

---


## ratelimitexceedederror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object RateLimitExceededError
```

## 

For more information, including a list of endpoints and their rate limits, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/identifying-rate-limits](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/identifying-rate-limits).

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## receiptCreationDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp receiptCreationDate
```

## 

For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSAppTransactionDecodedPayload).

## See Also

- [signedDate](../com.apple.appstoreserverapi/AppStoreServerAPI/signedDate.md)

---


## recentsubscriptionstartdate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp recentSubscriptionStartDate
```

## 

The recent subscription start date is in UNIX time, in milliseconds.

Use the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) to identify the earliest start date of a subscription in a series of auto-renewable subscription purchases that the customer maintained continuously, or that has one or more gaps of less than 60 days each.

The App Store calculates the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) by finding the start date of the most recent auto-renewable subscription purchase that’s preceded by a gap in paid service of more than 60 days in the production environment, or 10 minutes in the sandbox environment. The start date includes any free trials or promotional purchases. If no such gap exists — for example, if the user has only ever purchased one subscription — the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) is the same as the subscription’s [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalPurchaseDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalPurchaseDate).

The [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) calculation counts a grace period or a billing retry state as a gap in the paid service.

> **IMPORTANT:** Don’t use the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) date to calculate days of paid service. For more information about paid days of service, see [https://developer.apple.com/app-store/subscriptions/#revenue-after-one-year](https://developer.apple.com/app-store/subscriptions/#revenue-after-one-year).

This date applies to active or expired subscriptions. For example, if a subscriber purchases an auto-renewable subscription on June 1, 2022 and lets it expire on December 31, 2022, the App Store determines the recent subscription start date as follows:

- Initially, the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) is the same as the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalPurchaseDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalPurchaseDate): June 1, 2022.
- If the customer purchases the subscription again on February 1, 2023, less than 60 days after the initial subscription expired, the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) remains June 1, 2022.
- If the customer purchases the subscription again on April 1, 2023, more than 60 days after the first subscription expired, the App Store updates the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate](doc://com.apple.documentation/documentation/AppStoreServerNotifications/recentSubscriptionStartDate) to April 1, 2023.

## See Also

- [originalPurchaseDate](../com.apple.appstoreserverapi/AppStoreServerAPI/originalPurchaseDate.md)
- [purchaseDate](../com.apple.appstoreserverapi/AppStoreServerAPI/purchaseDate.md)

---


## refundPreference

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string refundPreference
```

## 

Use these values in the `refundPreference` field of a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest).

The following constraints apply to the `GRANT_PRORATED` option:

- If the product is a consumable or non-consumable In-App Purchase or a non-renewing subscription, you may include a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage) value in the `ConsumptionRequest`.
- If the product is an auto-renewable subscription, don’t include a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage) value in the `ConsumptionRequest`. The system calculates the consumption automatically for auto-renewable subscriptions.

Your refund preference is one of a variety of factors that the App Store uses to inform its refund decisions.

## See Also

- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [consumptionPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionPercentage.md)
- [deliveryStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatus.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)

---


## refundhistoryresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object RefundHistoryResponse
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History) endpoint returns this response.

This response returns a maximum of 20 refunded transactions. If your customer has more than 20 refunded transactions, the `hasMore` value is `true`. Each response includes a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse/revision) token. Call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History) again with the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/RefundHistoryResponse/revision) token in the query to receive the next set of transactions. When the App Store has no more transactions to send, the `hasMore` value is `false`.

Consider storing the `revision` token from the last page of results with other customer account information. Use it at a later date when you call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History) to request any new refunded transactions since the last time you called the endpoint for the customer. By using the stored `revision` token, you can avoid fetching transactions you’ve already received.

## Topics

### Response data types

- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)
- [revision](../com.apple.appstoreserverapi/AppStoreServerAPI/revision.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

## See Also

- [Get-Refund-History](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History.md)

---


## refundpreferencev1

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 refundPreferenceV1
```

## 

Your refund preference is one of a variety of factors that the App Store uses to inform its refund decisions.

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)
- [userStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/userStatus.md)

---


## renewalDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp renewalDate
```

## 

The `renewalDate` is a value that’s always present in the payload for auto-renewable subscriptions, even for expired subscriptions. This date indicates the expiration date of the most recent auto-renewable subscription purchase, including renewals, and may be in the past. For subscriptions that renew successfully, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalDate) is the date when the subscription renews.

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## renewalPrice

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 renewalPrice
```

## 

This value represents the renewal price, in milliunits of the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency), of the auto-renewable subscription. One unit of the currency equals 1000 milliunits.

If the next billing period includes an offer specified by the [doc://com.apple.documentation/documentation/AppStoreServerNotifications/offerIdentifier](doc://com.apple.documentation/documentation/AppStoreServerNotifications/offerIdentifier), the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalPrice](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/renewalPrice) value reflects the discount.

> **IMPORTANT:** For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

To determine the storefront, use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefront) value in the transaction. Don’t use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/currency) value to infer the storefront.

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [status](../com.apple.appstoreserverapi/AppStoreServerAPI/status.md)

---


## request-a-test-notification

## 

Use this endpoint to test if your server is receiving [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications) at the URLs that you configured in App Store Connect. The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint prompts the App Store server to send your server a notification with the `TEST` [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/notificationType](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/notificationType). The App Store server sends the `TEST` notification to your production URL if you call this endpoint’s production URL; it sends it to your sandbox URL if you call this endpoint’s sandbox URL.

Although `TEST` is a version 2 notification, you can call this endpoint regardless of whether you configured your App Store Server Notifications URL in App Store Connect for version 1 or version 2. For more information about the configuration and enabling notifications, see [https://help.apple.com/app-store-connect/#/dev0067a330b](https://help.apple.com/app-store-connect/#/dev0067a330b) and [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).

This endpoint responds with a `testNotificationToken` in [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/SendTestNotificationResponse](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/SendTestNotificationResponse). To learn the result that the App Store server recorded when it attempted to send your server the `TEST` notification, call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status) endpoint with the `testNotificationToken`. Use the status information to troubleshoot your server if it’s unable to receive the `TEST` notification.

## See Also

- [Get-Test-Notification-Status](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Test-Notification-Status.md)
- [SendTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/SendTestNotificationResponse.md)
- [CheckTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/CheckTestNotificationResponse.md)

---


## requestidentifier

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string requestIdentifier
```

## 

You provide a `requestIdentifier` in the request body when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoints.

The API returns the same request identifier in its response, so you can match your request with the related response. The [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) also include this request identifier in notifications related to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint. For more information, see the `RENEWAL_EXTENSION` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType).

To resend the same request due to a timeout or other error, use the same request identifier. Otherwise, create a unique request identifer for each different subscription-renewal-date extension request.

> **IMPORTANT:** Provide a `UUID` value for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/requestIdentifier) when calling the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint.

The maximum string length is 128 characters.

## See Also

- [extendByDays](../com.apple.appstoreserverapi/AppStoreServerAPI/extendByDays.md)
- [extendReasonCode](../com.apple.appstoreserverapi/AppStoreServerAPI/extendReasonCode.md)

---


## revision

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string revision
```

## 

The App Store server returns a `revision` value in each response to certain endpoints, such as [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Refund-History). Use the `revision` value to get a set of paginated transactions.

The first time you call an endpoint, you don’t include a `revision` query parameter, and the API returns the customer’s first set of up to 20 transactions. If there are more transactions, the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore) value in the response is `true`. To get the next set of transactions, use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revision](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revision) value from the response in your subsequent call to the endpoint.

Consider storing the `revision` value from the last page of transactions, when the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/hasMore) value is `false`, with other customer account information.  Use it the next time you call the endpoint for the same customer, to avoid fetching transactions you’ve already received. For the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Transaction-History) endpoint, store the `revision` value only if you request the transaction history in `ASCENDING` sort order.

## See Also

- [appAppleId](../com.apple.appstoreserverapi/AppStoreServerAPI/appAppleId.md)
- [bundleId](../com.apple.appstoreserverapi/AppStoreServerAPI/bundleId.md)
- [environment](../com.apple.appstoreserverapi/AppStoreServerAPI/environment.md)
- [hasMore](../com.apple.appstoreserverapi/AppStoreServerAPI/hasMore.md)
- [JWSTransaction](../com.apple.appstoreserverapi/AppStoreServerAPI/JWSTransaction.md)

---


## revocationDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp revocationDate
```

## See Also

- [revocationReason](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationReason.md)
- [revocationPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationPercentage.md)
- [revocationType](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationType.md)

---


## revocationType

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string revocationType
```

## 

If the `revocationType` is `REFUND_PRORATED`, see the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/revocationPercentage) for the prorated percentage.

## See Also

- [revocationDate](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationDate.md)
- [revocationReason](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationReason.md)
- [revocationPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationPercentage.md)

---


## revocationpercentage

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 revocationPercentage
```

## 

The revocation percentage value is rounded to three decimal places of precision, and is expressed as an integer, in milliunits. This field is present in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) for refunded transactions. This field doesn’t appear if the refund is reversed.

The following table shows several examples of revocation percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
| --- | --- |
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

## See Also

- [revocationDate](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationDate.md)
- [revocationReason](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationReason.md)
- [revocationType](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationType.md)

---


## revocationreason

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 revocationReason
```

## 

For Family Sharing transactions, the revocation reason value is `0` if the customer leaves the family group or the owner stops sharing. If the purchaser of a Family Sharing transaction receives a refund, the revocation reason for Family Sharing transactions matches the value of the purchaser’s revocation reason.

## See Also

- [revocationDate](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationDate.md)
- [revocationPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationPercentage.md)
- [revocationType](../com.apple.appstoreserverapi/AppStoreServerAPI/revocationType.md)

---


## samplecontentprovided

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean sampleContentProvided
```

## 

Set this value to `true` if you provided any of the following prior to the customer’s purchase:

- A free sample or free trial of the purchased content
- Information about the content and how it works, such as expected game play

Set this value to `false` otherwise.

## See Also

- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [consumptionPercentage](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionPercentage.md)
- [deliveryStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatus.md)
- [refundPreference](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreference.md)

---


## send-consumption-information-v1

## 

The App Store uses a variety of factors to determine if a refund request is approved or denied. To help inform and improve the refund process, you can send information about a customer’s consumption of the In-App Purchase to the App Store when the customer requests a refund. The App Store uses the consumption information you provide to inform its refund decisions.

When a customer initiates a refund request for a consumable In-App Purchase or auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) to your server through your [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint. If the customer provided consent, respond by calling this API and sending the consumption data in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequestV1) to the App Store. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

Respond within 12 hours of receiving the `CONSUMPTION_REQUEST` notification.

For information about configuring your server to receive App Store server notifications, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). For information about initiating refund requests in an app, see any of the refund request methods, including [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj), [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph), [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd), and [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-9mscy](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-9mscy).

### 

You must obtain valid consent from the customer before sharing their personal data with Apple in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API. You, the developer, are solely responsible for obtaining valid consent because you’re sharing with Apple the data that you collected from the customer.

The requirements to obtain valid consent vary under applicable law, and Apple can’t advise you on specific ways to obtain valid consent. Developers are responsible for determining specific compliance with applicable laws. If your app violates Apple’s guidelines, App Review will reach out and work with you to address any concerns.

Here are some general guidelines to keep in mind for obtaining valid consent:

- Valid consent is freely given, specific, informed, and unambiguous as to a customer’s wishes with respect to their personal data.
- As an example, when requesting consent, you may include: clear language that conveys to a customer that you will provide Apple with some of their personal data to assist with reviewing the customer’s app refund requests; clear language that conveys to customers that they can withdraw their consent at any time; and a method for customers to give their affirmative consent.
- Opt-in consent is a higher standard for consent than offering an opt-out. Generally, if you don’t offer an individual the opportunity to opt out, it can be difficult to show that consent is freely given.
- After you’ve obtained consent, if there is a change in circumstances causing you to conclude that the customer’s consent is no longer valid — for example, due to a change in the way you use or share data, or if the customer withdraws consent for this purpose — you should update the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented) flag and not send any further data from that customer.

> **IMPORTANT:** Don’t use the [doc://com.apple.documentation/documentation/AppTrackingTransparency](doc://com.apple.documentation/documentation/AppTrackingTransparency) prompt to obtain consent for sharing data with Apple through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API. Obtaining consent needed to use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) endpoint is unrelated to [doc://com.apple.documentation/documentation/AppTrackingTransparency](doc://com.apple.documentation/documentation/AppTrackingTransparency). These two features are distinct and unrelated.

The data you share with Apple through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API isn’t used for tracking. You must separately obtain consent from customers when sharing data with Apple using the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API.

### 

If you adopt the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API, answer the app privacy questions to disclose in your labels any data you collect from your customers and what you’re using it for. For more information about app privacy labels, see [https://developer.apple.com/app-store/app-privacy-details/](https://developer.apple.com/app-store/app-privacy-details/).

Apple uses and protects the data you share through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API in accordance with [https://www.apple.com/legal/privacy/en-ww/](https://www.apple.com/legal/privacy/en-ww/). For additional information about how Apple protects data, see [https://support.apple.com/guide/security/welcome/web](https://support.apple.com/guide/security/welcome/web). Apple retains the data you provide through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API for the period necessary to fulfill the purpose for which the data was collected, which is to improve the refund process by obtaining data that assists with reviewing the customer’s refund request. Apple may share the data you provide through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information-V1) API with service providers who act on our behalf, our partners, or others at your direction. Apple will not share the data with third parties for their own marketing purposes. For more information, see [https://www.apple.com/legal/privacy/data/en/app-store/](https://www.apple.com/legal/privacy/data/en/app-store/).

### 

If your customers request access to or deletion of their personal data related to consumption information, inform them that they may submit requests directly to Apple by visiting [https://privacy.apple.com](https://privacy.apple.com). If your app stores data in CloudKit on behalf of your customers, see [doc://com.apple.documentation/documentation/CloudKit/responding-to-requests-to-delete-data](doc://com.apple.documentation/documentation/CloudKit/responding-to-requests-to-delete-data), [doc://com.apple.documentation/documentation/CloudKit/providing-user-access-to-cloudkit-data](doc://com.apple.documentation/documentation/CloudKit/providing-user-access-to-cloudkit-data), and [doc://com.apple.documentation/documentation/CloudKit/changing-access-controls-on-user-data](doc://com.apple.documentation/documentation/CloudKit/changing-access-controls-on-user-data) for more information.

## See Also

- [Get-Transaction-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Transaction-History-V1.md)
- [Get-Refund-History-V1](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Refund-History-V1.md)
- [ConsumptionRequestV1](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequestV1.md)
- [RefundLookupResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/RefundLookupResponse.md)

---


## send-consumption-information

## 

The App Store uses a variety of factors to determine if a refund request is approved or denied. To help inform and improve the refund process, you can send information about a customer’s consumption of the In-App Purchase to the App Store when the customer requests a refund. The App Store uses the consumption information you provide to inform its refund decisions.

When a customer initiates a refund request for any product type (consumable, non-consumable, non-renewing subscription, or auto-renewable subscription), the App Store sends a `CONSUMPTION_REQUEST` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) to your server through your [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint. If the customer provided consent, respond by calling this API and sending the consumption data in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/ConsumptionRequest) to the App Store. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

Respond within 12 hours of receiving the `CONSUMPTION_REQUEST` notification.

For information about configuring your server to receive App Store server notifications, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). For information about initiating refund requests in an app, see any of the refund request methods, including [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj), [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph), [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd), and [doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-9mscy](doc://com.apple.documentation/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-9mscy).

### 

You must obtain valid consent from the customer before sharing their personal data with Apple in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API. You, the developer, are solely responsible for obtaining valid consent because you’re sharing with Apple the data that you collected from the customer.

The requirements to obtain valid consent vary under applicable law, and Apple can’t advise you on specific ways to obtain valid consent. Developers are responsible for determining specific compliance with applicable laws. If your app violates Apple’s guidelines, App Review will reach out and work with you to address any concerns.

Here are some general guidelines to keep in mind for obtaining valid consent:

- Valid consent is freely given, specific, informed, and unambiguous as to a customer’s wishes with respect to their personal data.
- As an example, when requesting consent, you may include: clear language that conveys to a customer that you will provide Apple with some of their personal data to assist with reviewing the customer’s app refund requests; clear language that conveys to customers that they can withdraw their consent at any time; and a method for customers to give their affirmative consent.
- Opt-in consent is a higher standard for consent than offering an opt-out. Generally, if you don’t offer an individual the opportunity to opt out, it can be difficult to show that consent is freely given.
- After you’ve obtained consent, if there is a change in circumstances causing you to conclude that the customer’s consent is no longer valid — for example, due to a change in the way you use or share data, or if the customer withdraws consent for this purpose — you should update the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/customerConsented) flag and not send any further data from that customer.

> **IMPORTANT:** Don’t use the [doc://com.apple.documentation/documentation/AppTrackingTransparency](doc://com.apple.documentation/documentation/AppTrackingTransparency) prompt to obtain consent for sharing data with Apple through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API. Obtaining consent needed to use the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) endpoint is unrelated to [doc://com.apple.documentation/documentation/AppTrackingTransparency](doc://com.apple.documentation/documentation/AppTrackingTransparency). These two features are distinct and unrelated.

The data you share with Apple through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API isn’t used for tracking. You must separately obtain consent from customers when sharing data with Apple using the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API.

### 

If you adopt the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API, answer the app privacy questions to disclose in your labels any data you collect from your customers and what you’re using it for. For more information about app privacy labels, see [https://developer.apple.com/app-store/app-privacy-details/](https://developer.apple.com/app-store/app-privacy-details/).

Apple uses and protects the data you share through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API in accordance with [https://www.apple.com/legal/privacy/en-ww/](https://www.apple.com/legal/privacy/en-ww/). For additional information about how Apple protects data, see [https://support.apple.com/guide/security/welcome/web](https://support.apple.com/guide/security/welcome/web). Apple retains the data you provide through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API for the period necessary to fulfill the purpose for which the data was collected, which is to improve the refund process by obtaining data that assists with reviewing the customer’s refund request. Apple may share the data you provide through the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Send-Consumption-Information) API with service providers who act on our behalf, our partners, or others at your direction. Apple will not share the data with third parties for their own marketing purposes. For more information, see [https://www.apple.com/legal/privacy/data/en/app-store/](https://www.apple.com/legal/privacy/data/en/app-store/).

### 

If your customers request access to or deletion of their personal data related to consumption information, inform them that they may submit requests directly to Apple by visiting [https://privacy.apple.com](https://privacy.apple.com). If your app stores data in CloudKit on behalf of your customers, see [doc://com.apple.documentation/documentation/CloudKit/responding-to-requests-to-delete-data](doc://com.apple.documentation/documentation/CloudKit/responding-to-requests-to-delete-data), [doc://com.apple.documentation/documentation/CloudKit/providing-user-access-to-cloudkit-data](doc://com.apple.documentation/documentation/CloudKit/providing-user-access-to-cloudkit-data), and [doc://com.apple.documentation/documentation/CloudKit/changing-access-controls-on-user-data](doc://com.apple.documentation/documentation/CloudKit/changing-access-controls-on-user-data) for more information.

## See Also

- [ConsumptionRequest](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionRequest.md)

---


## sendAttemptItem

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object sendAttemptItem
```

## Topics

### Data types

- [attemptDate](../com.apple.appstoreserverapi/AppStoreServerAPI/attemptDate.md)
- [sendAttemptResult](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptResult.md)

## See Also

- [signedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/signedPayload.md)

---


## sendAttemptResult

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string sendAttemptResult
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Notification-History) and [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status) endpoints return a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptResult](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptResult) for each notification attempt in their responses. This value describes the success or error the server encountered on its attempt to send the notification to your server.

In the production environment, the App Store server retries sending the notfications if it doesn’t receive a `200` response from your server. Your server may have successfully received the notification on the App Store server’s subsequent attempt if the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptResult](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/sendAttemptResult) value shows an error.

In the sandbox environment, the App Store server attempts to send the notification one time.

For more information about the timing of retry attempts, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/responding-to-app-store-server-notifications).

## See Also

- [sendAttemptItem](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptItem.md)
- [signedPayload](../com.apple.appstoreserverapi/AppStoreServerAPI/signedPayload.md)

---


## sendtestnotificationresponse

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object SendTestNotificationResponse
```

## 

The [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint returns this response, which includes a [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/SendTestNotificationResponse/testNotificationToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/SendTestNotificationResponse/testNotificationToken) value to reference the test associated with your request. When you request a test notification, the App Store server sends a notification with the `TEST` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) to your server. To learn the result of the App Store server’s attempt to send the `TEST` notification, call [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status) with the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/SendTestNotificationResponse/testNotificationToken](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/SendTestNotificationResponse/testNotificationToken).

For more information about notifications, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications).

## Topics

### Data types

- [testNotificationToken](../com.apple.appstoreserverapi/AppStoreServerAPI/testNotificationToken.md)

## See Also

- [Request-a-Test-Notification](../com.apple.appstoreserverapi/AppStoreServerAPI/Request-a-Test-Notification.md)
- [Get-Test-Notification-Status](../com.apple.appstoreserverapi/AppStoreServerAPI/Get-Test-Notification-Status.md)
- [CheckTestNotificationResponse](../com.apple.appstoreserverapi/AppStoreServerAPI/CheckTestNotificationResponse.md)

---


## signedDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp signedDate
```

## See Also

- [receiptCreationDate](../com.apple.appstoreserverapi/AppStoreServerAPI/receiptCreationDate.md)

---


## signedPayload

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string signedPayload
```

## 

The `signedpayload` is a string of three Base64 URL-encoded components, separated by a period.

For more information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/signedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/signedPayload) in [doc://com.apple.documentation/documentation/AppStoreServerNotifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications).

## See Also

- [sendAttemptItem](../com.apple.appstoreserverapi/AppStoreServerAPI/sendAttemptItem.md)

---


## simplifying-your-implementation-by-using-the-app-store-server-library

## 

The App Store Server Library is an open source library from Apple, available in four languages. It makes adopting the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) and working with JSON Web Signature (JWS) transactions easier. Find the App Store Server Library for each language in the following GitHub repositories:

- Swift: [https://github.com/apple/app-store-server-library-swift](https://github.com/apple/app-store-server-library-swift)
- Java: [https://github.com/apple/app-store-server-library-java](https://github.com/apple/app-store-server-library-java)
- Python: [https://github.com/apple/app-store-server-library-python](https://github.com/apple/app-store-server-library-python)
- Node: [https://github.com/apple/app-store-server-library-node](https://github.com/apple/app-store-server-library-node)

Choose the language that best supports your server and expertise.

The App Store Server Library offers the following capabilities:

- An API client that encodes [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI) requests, decodes the responses, and creates the JSON Web Token (JWT) you use to authenticate the calls. For more information on using JWTs, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests).
- Functions that verify JWS transactions, to verify that Apple signed the transaction data you get in API responses, from [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) and from devices using [doc://com.apple.documentation/documentation/StoreKit](doc://com.apple.documentation/documentation/StoreKit). See the functions `verifyAndDecodeTransaction`, `verifyAndDecodeAppTransaction`, and `verifyAndDecodeRenewalInfo`, available in each language the library supports.
- A utility that extracts transaction identifiers from receipts. The App Store Server API endpoints take a transaction identifier in the path parameter. Use this utility as you migrate from using [doc://com.apple.documentation/documentation/AppStoreReceipts/Verify-Receipt](doc://com.apple.documentation/documentation/AppStoreReceipts/Verify-Receipt) with [doc://com.apple.documentation/documentation/AppStoreReceipts](doc://com.apple.documentation/documentation/AppStoreReceipts) to using the App Store Server API for transaction information.
- A function that generates JWS signatures, which you use in your app for promotional offer signatures, Advanced Commerce API in-app requests, and introductory offer eligibility. For more information, see [doc://com.apple.documentation/documentation/StoreKit/generating-jws-to-sign-app-store-requests](doc://com.apple.documentation/documentation/StoreKit/generating-jws-to-sign-app-store-requests).

For more information, see the WWDC23 session [https://developer.apple.com/videos/play/wwdc2023/10143/](https://developer.apple.com/videos/play/wwdc2023/10143/).

## See Also

- [creating-api-keys-to-authorize-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
- [generating-json-web-tokens-for-api-requests](../com.apple.appstoreserverapi/AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
- [identifying-rate-limits](../com.apple.appstoreserverapi/AppStoreServerAPI/identifying-rate-limits.md)
- [app-store-server-api-changelog](../com.apple.appstoreserverapi/AppStoreServerAPI/app-store-server-api-changelog.md)

---


## startDate

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
timestamp startDate
```

## 

The start date must be earlier than the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/endDate](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/endDate).

## See Also

- [endDate](../com.apple.appstoreserverapi/AppStoreServerAPI/endDate.md)
- [notificationType](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationType.md)
- [notificationSubtype](../com.apple.appstoreserverapi/AppStoreServerAPI/notificationSubtype.md)
- [onlyFailures](../com.apple.appstoreserverapi/AppStoreServerAPI/onlyFailures.md)

---


## startdateafterenddateerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object StartDateAfterEndDateError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)
- [TestNotificationNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/TestNotificationNotFoundError.md)

---


## status

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 status
```

## 

For more information about the Billing Grace Period, see [https://help.apple.com/app-store-connect/#/dev58bda3212](https://help.apple.com/app-store-connect/#/dev58bda3212).

## See Also

- [autoRenewStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewStatus.md)
- [autoRenewProductId](../com.apple.appstoreserverapi/AppStoreServerAPI/autoRenewProductId.md)
- [expirationIntent](../com.apple.appstoreserverapi/AppStoreServerAPI/expirationIntent.md)
- [expiresDate](../com.apple.appstoreserverapi/AppStoreServerAPI/expiresDate.md)
- [isUpgraded](../com.apple.appstoreserverapi/AppStoreServerAPI/isUpgraded.md)
- [renewalDate](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalDate.md)
- [renewalPrice](../com.apple.appstoreserverapi/AppStoreServerAPI/renewalPrice.md)

---


## storefront

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string storefront
```

## 

This property uses the ISO 3166-1 alpha-3 country code representation. This property is the same as the [doc://com.apple.documentation/documentation/StoreKit/Storefront/countryCode](doc://com.apple.documentation/documentation/StoreKit/Storefront/countryCode) in StoreKit.

## See Also

- [storefrontId](../com.apple.appstoreserverapi/AppStoreServerAPI/storefrontId.md)

---


## storefrontId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string storefrontId
```

## 

This value is the same as the [doc://com.apple.documentation/documentation/storekit/storefront/id-n42](doc://com.apple.documentation/documentation/storekit/storefront/id-n42) value in StoreKit.

## See Also

- [storefront](../com.apple.appstoreserverapi/AppStoreServerAPI/storefront.md)

---


## storefrontcountrycode

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string storefrontCountryCode
```

## 

This type uses the ISO 3166-1 Alpha-3 country code representation.

## See Also

- [extendByDays](../com.apple.appstoreserverapi/AppStoreServerAPI/extendByDays.md)
- [extendReasonCode](../com.apple.appstoreserverapi/AppStoreServerAPI/extendReasonCode.md)
- [productId](../com.apple.AppStoreServerNotifications/productId.md)
- [requestIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/requestIdentifier.md)
- [storefrontCountryCodes](../com.apple.appstoreserverapi/AppStoreServerAPI/storefrontCountryCodes.md)

---


## storefrontcountrycodes

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
[storefrontCountryCode] storefrontCountryCodes
```

## 

You provide the list of storefront country codes in the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest) to limit the storefronts in which the App Store extends the subscription renewal date. To indicate that the extension applies in all storefronts, omit the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefrontCountryCodes](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/storefrontCountryCodes) object from the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest) object.

## See Also

- [extendByDays](../com.apple.appstoreserverapi/AppStoreServerAPI/extendByDays.md)
- [extendReasonCode](../com.apple.appstoreserverapi/AppStoreServerAPI/extendReasonCode.md)
- [productId](../com.apple.AppStoreServerNotifications/productId.md)
- [requestIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/requestIdentifier.md)
- [storefrontCountryCode](../com.apple.appstoreserverapi/AppStoreServerAPI/storefrontCountryCode.md)

---


## subscriptionGroupIdentifier

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string subscriptionGroupIdentifier
```

## 

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [https://help.apple.com/app-store-connect/#/dev75708c031](https://help.apple.com/app-store-connect/#/dev75708c031).

## See Also

- [productId](../com.apple.appstoreserverapi/AppStoreServerAPI/productId.md)
- [type](../com.apple.appstoreserverapi/AppStoreServerAPI/type.md)
- [quantity](../com.apple.appstoreserverapi/AppStoreServerAPI/quantity.md)

---


## subscriptionextensionineligibleerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object SubscriptionExtensionIneligibleError
```

## 

This error applies to the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Extend-a-Subscription-Renewal-Date) endpoint.

Auto-renewable subscriptions in the following states aren’t eligible for renewal date extensions:

- Subscriptions in a free offer period
- Inactive subscriptions in a billing retry state
- Subscriptions in a grace period state with an expiration date in the past
- Subscriptions that have already received two renewal date extensions within the past 365 days
- Expired subscriptions

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## succeededcount

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int64 succeededCount
```

## 

For information about a subscription’s eligibility to receive a subscription-renewal-date extension, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/extending-the-renewal-date-for-auto-renewable-subscriptions).

## See Also

- [complete](../com.apple.appstoreserverapi/AppStoreServerAPI/complete.md)
- [completeDate](../com.apple.appstoreserverapi/AppStoreServerAPI/completeDate.md)
- [failedCount](../com.apple.appstoreserverapi/AppStoreServerAPI/failedCount.md)

---


## success

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
boolean success
```

## 

If this value is `true`, the renewal date for the subscription is extended.

## See Also

- [effectiveDate](../com.apple.appstoreserverapi/AppStoreServerAPI/effectiveDate.md)
- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [webOrderLineItemId](../com.apple.appstoreserverapi/AppStoreServerAPI/webOrderLineItemId.md)

---


## testNotificationToken

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string testNotificationToken
```

## 

You receive a `testNotificationToken` when you call the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Request-a-Test-Notification) endpoint. Use the `testNotificationToken` to learn your server’s response to the test by calling [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Get-Test-Notification-Status).

---


## testnotificationnotfounderror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object TestNotificationNotFoundError
```

## See Also

- [InvalidEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEndDateError.md)
- [InvalidNotificationTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidNotificationTypeError.md)
- [InvalidPaginationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPaginationTokenError.md)
- [InvalidStartDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidStartDateError.md)
- [InvalidTestNotificationTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTestNotificationTokenError.md)
- [InvalidInAppOwnershipTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidInAppOwnershipTypeError.md)
- [InvalidProductIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductIdError.md)
- [InvalidProductTypeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidProductTypeError.md)
- [InvalidSortError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSortError.md)
- [InvalidSubscriptionGroupIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSubscriptionGroupIdentifierError.md)
- [MultipleFiltersSuppliedError](../com.apple.appstoreserverapi/AppStoreServerAPI/MultipleFiltersSuppliedError.md)
- [PaginationTokenExpiredError](../com.apple.appstoreserverapi/AppStoreServerAPI/PaginationTokenExpiredError.md)
- [ServerNotificationURLNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/ServerNotificationURLNotFoundError.md)
- [StartDateAfterEndDateError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateAfterEndDateError.md)
- [StartDateTooFarInPastError](../com.apple.appstoreserverapi/AppStoreServerAPI/StartDateTooFarInPastError.md)

---


## transactionId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string transactionId
```

## 

In a purchase transaction, the `transactionId` matches the original transaction identifier, [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/originalTransactionId). When a customer restores a purchase or renews a subscription, the `transactionId` differs.

## See Also

- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [webOrderLineItemId](../com.apple.appstoreserverapi/AppStoreServerAPI/webOrderLineItemId.md)

---


## transactionidnotfounderror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object TransactionIdNotFoundError
```

## 

Don’t unlock the service or content associated with the transaction ID for the app bundle ID and environment that you indicate in the request unless you successfully resolve this error. To resolve this error, check your request to ensure that:

- The JSON Web Token (JWT) payload contains the bundle ID (`bid`) of your app that’s associated with the transaction ID. For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests).
- You’re making the request in the same environment, production or sandbox, that generated the transaction ID.

In rare cases, you might get this error for transaction IDs that previously returned data successfully. Don’t unlock the service or content for the app bundle ID and environment in the request if you’re unable to resolve this error using the steps above.

## See Also

- [AccountNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AccountNotFoundError.md)
- [AdvancedCommerceTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AdvancedCommerceTransactionNotSupportedError.md)
- [AppNotFoundError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppNotFoundError.md)
- [AppTransactionDoesNotExistError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionDoesNotExistError.md)
- [AppTransactionIdNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/AppTransactionIdNotSupportedError.md)
- [FamilySharedSubscriptionExtensionIneligibleError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilySharedSubscriptionExtensionIneligibleError.md)
- [FamilyTransactionNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/FamilyTransactionNotSupportedError.md)
- [GeneralInternalError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralInternalError.md)
- [GeneralBadRequestError](../com.apple.appstoreserverapi/AppStoreServerAPI/GeneralBadRequestError.md)
- [InvalidAppAccountTokenUUIDError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenUUIDError.md)
- [InvalidAppIdentifierError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppIdentifierError.md)
- [InvalidEmptyStorefrontCountryCodeListError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidEmptyStorefrontCountryCodeListError.md)
- [InvalidExtendByDaysError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendByDaysError.md)
- [InvalidExtendReasonCodeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidExtendReasonCodeError.md)
- [InvalidOriginalTransactionIdError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidOriginalTransactionIdError.md)

---


## transactionreason

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string transactionReason
```

## 

If a customer upgrades an auto-renewable subscription, the upgrade is effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change occurs on the subscription renewal date. The resulting `transactionReason` is `RENEWAL`.

---


## type

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string type
```

## See Also

- [productId](../com.apple.appstoreserverapi/AppStoreServerAPI/productId.md)
- [subscriptionGroupIdentifier](../com.apple.appstoreserverapi/AppStoreServerAPI/subscriptionGroupIdentifier.md)
- [quantity](../com.apple.appstoreserverapi/AppStoreServerAPI/quantity.md)

---


## undeliveredconsumptionpercentagenonzeroerror

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object UndeliveredConsumptionPercentageNonZeroError
```

## 

For more information, see [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/consumptionPercentage).

## See Also

- [ConsumptionPercentageAutoRenewableSubscriptionError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageAutoRenewableSubscriptionError.md)
- [ConsumptionPercentageOutOfRangeError](../com.apple.appstoreserverapi/AppStoreServerAPI/ConsumptionPercentageOutOfRangeError.md)
- [InvalidAccountTenureError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAccountTenureError.md)
- [InvalidAppAccountTokenError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidAppAccountTokenError.md)
- [InvalidConsumptionStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidConsumptionStatusError.md)
- [InvalidCustomerConsentedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidCustomerConsentedError.md)
- [InvalidDeliveryStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidDeliveryStatusError.md)
- [InvalidLifetimeDollarsPurchasedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsPurchasedError.md)
- [InvalidLifetimeDollarsRefundedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidLifetimeDollarsRefundedError.md)
- [InvalidPlatformError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlatformError.md)
- [InvalidPlayTimeError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidPlayTimeError.md)
- [InvalidSampleContentProvidedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidSampleContentProvidedError.md)
- [InvalidTransactionTypeNotSupportedError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionTypeNotSupportedError.md)
- [InvalidUserStatusError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidUserStatusError.md)
- [InvalidTransactionNotConsumableError](../com.apple.appstoreserverapi/AppStoreServerAPI/InvalidTransactionNotConsumableError.md)

---


## updateappaccounttokenrequest

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
object UpdateAppAccountTokenRequest
```

## 

This is the request body for the [doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token](doc://com.apple.appstoreserverapi/documentation/AppStoreServerAPI/Set-App-Account-Token) endpoint.

## See Also

- [Set-App-Account-Token](../com.apple.appstoreserverapi/AppStoreServerAPI/Set-App-Account-Token.md)

---


## userStatus

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
int32 userStatus
```

## 

This user status represents the standing of a customer account in your app.

## See Also

- [accountTenure](../com.apple.appstoreserverapi/AppStoreServerAPI/accountTenure.md)
- [appAccountToken](../com.apple.appstoreserverapi/AppStoreServerAPI/appAccountToken.md)
- [consumptionStatus](../com.apple.appstoreserverapi/AppStoreServerAPI/consumptionStatus.md)
- [customerConsented](../com.apple.appstoreserverapi/AppStoreServerAPI/customerConsented.md)
- [deliveryStatusV1](../com.apple.appstoreserverapi/AppStoreServerAPI/deliveryStatusV1.md)
- [lifetimeDollarsPurchased](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsPurchased.md)
- [lifetimeDollarsRefunded](../com.apple.appstoreserverapi/AppStoreServerAPI/lifetimeDollarsRefunded.md)
- [platform](../com.apple.appstoreserverapi/AppStoreServerAPI/platform.md)
- [playTime](../com.apple.appstoreserverapi/AppStoreServerAPI/playTime.md)
- [refundPreferenceV1](../com.apple.appstoreserverapi/AppStoreServerAPI/refundPreferenceV1.md)
- [sampleContentProvided](../com.apple.appstoreserverapi/AppStoreServerAPI/sampleContentProvided.md)

---


## webOrderLineItemId

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
string webOrderLineItemId
```

## 

This value applies only to auto-renewable subscriptions.

## See Also

- [effectiveDate](../com.apple.appstoreserverapi/AppStoreServerAPI/effectiveDate.md)
- [originalTransactionId](../com.apple.appstoreserverapi/AppStoreServerAPI/originalTransactionId.md)
- [success](../com.apple.appstoreserverapi/AppStoreServerAPI/success.md)

---


## x5c

## Declaration

**Platforms:** Unsupported OS: App Store Server API

```swift
[string] x5c
```

## 

For more information, or to download Apple’s root and intermediate certificates, see [https://www.apple.com/certificateauthority/](https://www.apple.com/certificateauthority/).

## See Also

- [alg](../com.apple.appstoreserverapi/AppStoreServerAPI/alg.md)

---

