# advancedcommerceapi

*Merged documentation for advancedcommerceapi*

---

# Advanced Commerce API

## 

Use this framework to offer an exceptionally large catalog of one-time purchases, subscriptions, and subscriptions with optional add-ons while using the App Store commerce system. Apps that use this API host and manage their own catalog of In-App Purchases, or SKUs. The App Store commerce system handles the end-to-end payment processing, global distribution, tax support, and customer service.

You can use the Advanced Commerce API and the StoreKit [doc://com.apple.documentation/documentation/StoreKit/in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/in-app-purchase) API in the same app. Both APIs use the App Store commerce system, including the same signed JWS transactions and JWS renewal info. For products that you offer using the In-App Purchase API, you set up product identifiers in App Store Connect. For products that you offer using the Advanced Commerce API, you host and manage your own catalog of SKUs and add product details dynamically at runtime. For complete setup information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce).

Advanced Commerce API features are available through requests you make using StoreKit in your app and endpoint requests from your server. To authorize these requests, you generate JSON Web Tokens (JWTs). The App Store Server Library provides a client that makes it easier to create JWTs to authorize calls. For more information about the library, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.documentation/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library). For more information about authorizing calls, see  [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/authorizing-server-calls](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/authorizing-server-calls).

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to call the Advanced Commerce API.

> **IMPORTANT:** To learn more about eligibility and apply for access to the Advanced Commerce API, see [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). For more about eligibility and to apply for access to the Mini Apps Partner Program, see [https://developer.apple.com/programs/mini-apps-partner/](https://developer.apple.com/programs/mini-apps-partner/).

## Topics

### Essentials

- [setting-up-your-project-for-advanced-commerce](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce.md)
- [setupmanagesubscriptions](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setupmanagesubscriptions.md)
- [changelog](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/changelog.md)

### API authorization and rate limits

- [authorizing-server-calls](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/authorizing-server-calls.md)
- [ratelimits](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ratelimits.md)

### Generic product IDs and SKUs

- [setting-up-generic-product-identifiers](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setting-up-generic-product-identifiers.md)
- [creating-your-purchases](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/creating-your-purchases.md)
- [creating-skus-for-the-mini-app-partner-program](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/creating-skus-for-the-mini-app-partner-program.md)

### Tax codes and pricing

- [prices](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/prices.md)
- [taxcodes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxcodes.md)
- [handling-subscription-price-changes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/handling-subscription-price-changes.md)

### In-app API requests

- [sending-advanced-commerce-api-requests-from-your-app](../com.apple.StoreKit/sending-advanced-commerce-api-requests-from-your-app.md)
- [generating-jws-to-sign-app-store-requests](../com.apple.StoreKit/generating-jws-to-sign-app-store-requests.md)

### One-time charge creation in the app

- [OneTimeChargeCreateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OneTimeChargeCreateRequest.md)
- [OneTimeChargeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OneTimeChargeItem.md)

### Subscription creation in the app

- [SubscriptionCreateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCreateRequest.md)
- [SubscriptionCreateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCreateItem.md)

### Subscription modification in the app

- [SubscriptionModifyInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyInAppRequest.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)

### Subscription reactivation in the app

- [SubscriptionReactivateInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest.md)
- [SubscriptionReactivateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionReactivateItem.md)

### Subscription price change from the server

- [Change-Subscription-Price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Price.md)
- [SubscriptionPriceChangeRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeRequest.md)
- [SubscriptionPriceChangeResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeResponse.md)

### Subscription cancellation from the server

- [Cancel-a-Subscription](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Cancel-a-Subscription.md)
- [SubscriptionCancelRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCancelRequest.md)
- [SubscriptionCancelResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCancelResponse.md)

### Subscription revocation from the server

- [Revoke-Subscription](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Revoke-Subscription.md)
- [SubscriptionRevokeRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionRevokeRequest.md)
- [SubscriptionRevokeResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionRevokeResponse.md)

### Refund request from the server

- [Request-Transaction-Refund](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Request-Transaction-Refund.md)
- [RequestRefundRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundRequest.md)
- [RequestRefundResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundResponse.md)
- [RequestRefundItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundItem.md)

### Subscription metadata changes from the server

- [Change-Subscription-Metadata](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Metadata.md)
- [SubscriptionChangeMetadataRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataRequest.md)
- [SubscriptionChangeMetadataResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataResponse.md)
- [SubscriptionChangeMetadataDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataDescriptors.md)
- [SubscriptionChangeMetadataItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataItem.md)

### Migration from the server

- [Migrate-Subscription-to-Advanced-Commerce-API](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API.md)
- [SubscriptionMigrateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRequest.md)
- [SubscriptionMigrateResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateResponse.md)
- [SubscriptionMigrateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateItem.md)
- [SubscriptionMigrateRenewalItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRenewalItem.md)
- [SubscriptionMigrateDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateDescriptors.md)

### Objects and types

- [datatypes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/datatypes.md)

### Signed transaction information

- [JWSRenewalInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/JWSRenewalInfo.md)
- [JWSTransaction](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/JWSTransaction.md)

### Error handling

- [errorcodes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/errorcodes.md)

---


# Detailed Documentation


## AtLeastOneOfDisplayNameOrDescriptionError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object AtLeastOneOfDisplayNameOrDescriptionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## Change-Subscription-Price

## 

Call this endpoint when you change the price of a subscription or any bundle or item within it. For information about the customer communication, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/handling-subscription-price-changes](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/handling-subscription-price-changes).

Only active subscriptions that aren’t in a billing retry state are eligible for price changes. When you call this endpoint, the price change takes effect at the next subscription renewal. Call the endpoint no later than 24 hours before the renewal date to have it take effect at the renewal.

For information about providing prices, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/prices](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/prices).

### 

In the following request:

- The subscription includes multiple items, and only one item has a price increase to USD 12.99.
- The price increase takes effect at the next subscription renewal.
- The decoded signed transaction shows price in the current period, before the increase.
- The decoded signed renewal information shows the increased price, which takes effect at the next renewal period if consented to.
- The item has a dependent SKU, which will be cancelled if the price increase is not agreed to.
- In this example, the price increase has been communicated, so the status is marked as pending.

## See Also

- [SubscriptionPriceChangeRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeRequest.md)
- [SubscriptionPriceChangeResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeResponse.md)

---


## DescriptionLengthExceededError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object DescriptionLengthExceededError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## Descriptors

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object Descriptors
```

## See Also

- [Offer](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Offer.md)
- [RequestInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestInfo.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyDescriptors.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionPriceChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeItem.md)

---


## DisplayNameLengthExceededError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object DisplayNameLengthExceededError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## GeneralInternalRetryableError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object GeneralInternalRetryableError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## InvalidAmountError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidAmountError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidCurrencyError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidCurrencyError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidDescriptionError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidDescriptionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidDisplayNameError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidDisplayNameError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidOfferPeriodCountError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidOfferPeriodCountError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidPreviousSubscriptionError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidPreviousSubscriptionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidProductError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidProductError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidRefundReasonError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidRefundReasonError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidRenewalPeriodError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidRenewalPeriodError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidSKUError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidSKUError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidSKUProvidedMustBeCurrentSKUSetToRenewError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidSKUProvidedMustBeCurrentSKUSetToRenewError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidSalableDurationError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidSalableDurationError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidSalableError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidSalableError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## InvalidTargetProductIDError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidTargetProductIDError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## ItemCannotBeSpecifiedMultipleTimesError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ItemCannotBeSpecifiedMultipleTimesError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## ItemLimitExceededError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ItemLimitExceededError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## JWSTransaction

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string JWSTransaction
```

### 

This `JWSTransaction` object is identical to the one used in the App Store Server API and by App Store Server Notifications. For details, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSTransaction](doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSTransaction).

## See Also

- [JWSRenewalInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/JWSRenewalInfo.md)

---


## MalformedPayloadError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MalformedPayloadError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## Migrate-Subscription-to-Advanced-Commerce-API

## 

> **NOTE:** You can use the Advanced Commerce API and the StoreKit [doc://com.apple.documentation/documentation/StoreKit/in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/in-app-purchase) APIs in the same app. Both APIs use the App Store commerce system, including the same signed JWS transactions and JWS renewal info. For products that you offer using the In-App Purchase API, you set up product identifiers in App Store Connect. For products that you offer using the Advanced Commerce API, you host and manage your own catalog of SKUs and add product details dynamically at runtime.

## See Also

- [SubscriptionMigrateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRequest.md)
- [SubscriptionMigrateResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateResponse.md)
- [SubscriptionMigrateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateItem.md)
- [SubscriptionMigrateRenewalItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRenewalItem.md)
- [SubscriptionMigrateDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateDescriptors.md)

---


## MissingPricingConfigForStorefrontError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MissingPricingConfigForStorefrontError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## MissingUpdatedItemsWithPeriodChangeError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MissingUpdatedItemsWithPeriodChangeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## MoreItemsThanAllowedError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MoreItemsThanAllowedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NegativeProratedPriceError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NegativeProratedPriceError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NegativeRefundAmountError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NegativeRefundAmountError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullAdvancedCommerceDataError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullAdvancedCommerceDataError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullDisplayNameError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullDisplayNameError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullItemError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullItemError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullItemsError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullItemsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullNewSKUError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullNewSKUError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullOfferPeriodError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullOfferPeriodError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullPeriodCountError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullPeriodCountError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullPriceError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullPriceError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullReasonError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullReasonError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullRefundAmountError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRefundAmountError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullRefundRiskingError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRefundRiskingError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullRequestReferenceIDError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRequestReferenceIDError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullRetainBillingCycleError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRetainBillingCycleError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## NullTargetProductIDError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullTargetProductIDError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## Offer

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object Offer
```

## See Also

- [Descriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Descriptors.md)
- [RequestInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestInfo.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyDescriptors.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionPriceChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeItem.md)

---


## OfferPreventsItemMidCycleChangeError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object OfferPreventsItemMidCycleChangeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## OneTimeChargeItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object OneTimeChargeItem
```

## See Also

- [OneTimeChargeCreateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OneTimeChargeCreateRequest.md)

---


## PendingChangesMismatchError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PendingChangesMismatchError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## PeriodChangeEffectiveConflictError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PeriodChangeEffectiveConflictError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## PeriodResetWithRetainBillingCycleError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PeriodResetWithRetainBillingCycleError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## PriceChangeNotSupportedThroughModifyItemsError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PriceChangeNotSupportedThroughModifyItemsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## ProductNotOwnedError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ProductNotOwnedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## ProratedOnlyLatestTransactionError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ProratedOnlyLatestTransactionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## RemoveItemsWithoutAddOrChangeItemsError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RemoveItemsWithoutAddOrChangeItemsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## RepeatedRequestReferenceIdError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RepeatedRequestReferenceIdError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## Request-Transaction-Refund

## 

> **NOTE:** To use the `Request Transaction Refund` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription), and `Request Transaction Refund` APIs.

## See Also

- [RequestRefundRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundRequest.md)
- [RequestRefundResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundResponse.md)
- [RequestRefundItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundItem.md)

---


## RequestInfo

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RequestInfo
```

## 

You provide the `RequestInfo` in your Advanced Commerce API server requests to uniquely identify your requests. You also have the option to provide additional data in the `RequestInfo` object.

### 

You can include an `appAccountToken` in `RequestInfo` to associate an account on your system with the purchase. The App Store returns the same `appAccountToken` value in the transaction information.

If you include `appAccountToken` in the `RequestInfo`, you don’t need to include the app account token as a purchase option by adding [doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)](doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) to the product purchase options ([doc://com.apple.documentation/documentation/StoreKit/Product/purchase(options:)](doc://com.apple.documentation/documentation/StoreKit/Product/purchase(options:))).

> **IMPORTANT:** If you do include `appAccountToken` in the `purchase(options:)`, you must include the same app account token value in the `RequestInfo`; otherwise, the request fails.

For more information about sending API requests from your app, see [doc://com.apple.documentation/documentation/StoreKit/sending-advanced-commerce-api-requests-from-your-app](doc://com.apple.documentation/documentation/StoreKit/sending-advanced-commerce-api-requests-from-your-app).

### 

The consistency token helps prevent unintended operations that might occur when the server gets multiple or overlapping requests for the same subscription.

Subscriptions receive a new consistency token in the [doc://com.apple.documentation/documentation/AppStoreServerAPI/advancedCommerceRenewalInfo](doc://com.apple.documentation/documentation/AppStoreServerAPI/advancedCommerceRenewalInfo) object of the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/JWSRenewalInfo](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/JWSRenewalInfo) each time the system updates the subscrpition renewal information. Include the consistency token when you use the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest) operation to resubscribe to the subscription and provide the `previousTransactionID`.

Don’t include a consistency token when:

- You haven’t received a consistency token.
- You’re using the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest) operation.
- You’re using the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest) operation for an initial subscription purchase.

## See Also

- [Descriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Descriptors.md)
- [Offer](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Offer.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyDescriptors.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionPriceChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeItem.md)

---


## Revoke-Subscription

## 

When this endpoint succeeds, the system sets the subscription’s auto-renew status to `false`, and revokes the subscription with a full or prorated refund. The App Store Server Notifications sends a `REFUND`  [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) to your [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint. Check the `revocationDate` property in the notification’s  [doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload](doc://com.apple.documentation/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload). Turn off service for the subscription and its items as of the revocation date. Don’t turn off service to the subscription until you receive the notification.

To cancel a subscription at the end of the current period instead, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription).

> **NOTE:** To use the `Revoke Subscription` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription), `Revoke Subscription`, and [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund) APIs.

## See Also

- [SubscriptionRevokeRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionRevokeRequest.md)
- [SubscriptionRevokeResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionRevokeResponse.md)

---


## RevokeOnInactiveSubscriptionError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RevokeOnInactiveSubscriptionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## SKU

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string SKU
```

### 

Apps that use the Advanced Commerce API manage their own catalogs of in-app purchases. You assign a SKU to each product, along with other information such as the display name, description, and price.

The SKU value isn’t displayed to customers, and isn’t stored by App Store Connect.

A SKU can represent any type of in-app purchase product that your app offers, including products with a one-time charge, auto-renewable subscriptions, or bundles and items in subscriptions.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## SubscriptionAlreadyActiveError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionAlreadyActiveError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## SubscriptionAlreadyMigratedError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionAlreadyMigratedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## SubscriptionChangeMetadataItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionChangeMetadataItem
```

## See Also

- [Change-Subscription-Metadata](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Metadata.md)
- [SubscriptionChangeMetadataRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataRequest.md)
- [SubscriptionChangeMetadataResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataResponse.md)
- [SubscriptionChangeMetadataDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataDescriptors.md)

---


## SubscriptionChangeMetadataRequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionChangeMetadataRequest
```

## See Also

- [Change-Subscription-Metadata](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Metadata.md)
- [SubscriptionChangeMetadataResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataResponse.md)
- [SubscriptionChangeMetadataDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataDescriptors.md)
- [SubscriptionChangeMetadataItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataItem.md)

---


## SubscriptionCreateRequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionCreateRequest
```

### 

### 

## See Also

- [SubscriptionCreateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCreateItem.md)

---


## SubscriptionMigrateDescriptors

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionMigrateDescriptors
```

## See Also

- [Migrate-Subscription-to-Advanced-Commerce-API](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API.md)
- [SubscriptionMigrateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRequest.md)
- [SubscriptionMigrateResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateResponse.md)
- [SubscriptionMigrateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateItem.md)
- [SubscriptionMigrateRenewalItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRenewalItem.md)

---


## SubscriptionMigrateRenewalItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionMigrateRenewalItem
```

## 

If you migrate a subscription that is to renew to another SKU, provide the item that is to renew in the `SubscriptionMigrateRenewalItem`.
For example, if a customer downgrades a subscription, the subscription continues unchanged until the end of the billing period, and downgrades when it renews. If you migrate a subscription in this state before the end of the billing period, you need to provide the item that renews.

## See Also

- [Migrate-Subscription-to-Advanced-Commerce-API](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API.md)
- [SubscriptionMigrateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRequest.md)
- [SubscriptionMigrateResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateResponse.md)
- [SubscriptionMigrateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateItem.md)
- [SubscriptionMigrateDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateDescriptors.md)

---


## SubscriptionMigrateResponse

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionMigrateResponse
```

## 

This is the response body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API) endpoint.

## See Also

- [Migrate-Subscription-to-Advanced-Commerce-API](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API.md)
- [SubscriptionMigrateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRequest.md)
- [SubscriptionMigrateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateItem.md)
- [SubscriptionMigrateRenewalItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRenewalItem.md)
- [SubscriptionMigrateDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateDescriptors.md)

---


## SubscriptionModifyAddItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionModifyAddItem
```

## See Also

- [SubscriptionModifyInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyInAppRequest.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)

---


## SubscriptionModifyDescriptors

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionModifyDescriptors
```

## See Also

- [Descriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Descriptors.md)
- [Offer](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Offer.md)
- [RequestInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestInfo.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionPriceChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeItem.md)

---


## SubscriptionModifyPeriodChange

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionModifyPeriodChange
```

## See Also

- [SubscriptionModifyInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyInAppRequest.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)

---


## SubscriptionModifyRemoveItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionModifyRemoveItem
```

## See Also

- [SubscriptionModifyInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyInAppRequest.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)

---


## SubscriptionNotEligibleError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionNotEligibleError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## SubscriptionPriceChangeItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionPriceChangeItem
```

## See Also

- [Descriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Descriptors.md)
- [Offer](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Offer.md)
- [RequestInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestInfo.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyDescriptors.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)

---


## SubscriptionReactivateItem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionReactivateItem
```

## 

This object is part of the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest) that your app uses to reactivate a subscription that would otherwise expire.

## See Also

- [SubscriptionReactivateInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest.md)

---


## SubscriptionRevokeRequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionRevokeRequest
```

## 

This is the request body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription) endpoint.

## See Also

- [Revoke-Subscription](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Revoke-Subscription.md)
- [SubscriptionRevokeResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionRevokeResponse.md)

---


## TransactionCannotBeRefundedContactSupportError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object TransactionCannotBeRefundedContactSupportError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## UnexpectedVersionError

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object UnexpectedVersionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## acapriceincreaseisnotcurrentlysupportedinindiaerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError
```

## See Also

- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## alreadyrefundederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object AlreadyRefundedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## atleastoneitemerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object AtLeastOneItemError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## authorizing-server-calls

## 

The following Advanced Commerce APIs are endpoints that you call from your server:

- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription)
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata)
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price)
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API)
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund)
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription)

Calls to the Advanced Commerce API’s endpoints require JSON Web Tokens (JWTs) for authorization; you obtain keys to create the tokens from your organization’s App Store Connect account. See [doc://com.apple.documentation/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests](doc://com.apple.documentation/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests) to create your keys. See [doc://com.apple.documentation/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests](doc://com.apple.documentation/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests) to generate tokens using your keys and send API requests.

After you have a complete and signed token, provide the token in the request’s authorization header as a bearer token. Generate a new token for each new API request, or reuse tokens until they expire.

> **TIP:** The App Store Server Library provides a client that makes it easier to adopt the Advanced Commerce APIs, including creating the JWTs to authorize calls. For more information, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library](doc://com.apple.documentation/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## See Also

- [ratelimits](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ratelimits.md)

---


## billingcycleresetwitheffectivelatererror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object BillingCycleResetWithEffectiveLaterError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## cancel-a-subscription

## 

When this endpoint succeeds, the system sets the subscription’s auto-renew status to `false` and the subscription doesn’t renew at the next renewal period. The customer continues to have access to the subscription until the end of the current period.

To immediately cancel a subscription instead, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription).

> **NOTE:** To use the `Cancel a Subscription` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the `Cancel a Subscription`, [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription), and [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund) APIs.

### 

## See Also

- [SubscriptionCancelRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCancelRequest.md)
- [SubscriptionCancelResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCancelResponse.md)

---


## change-subscription-metadata

## 

Use this endpoint to update the display name and description of an auto-renewable subscription. Calling this endpoint doesn’t change the price, billing details, or the service. For example, you can call `Change Subscription Metadata` if a subscription’s display name changes due to a change in its branding.

Don’t call this endpoint if a customer is changing subscriptions to receive a different service, such as upgrading, downgrading, or cross-grading. For such changes, use [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionModifyInAppRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionModifyInAppRequest).

## See Also

- [SubscriptionChangeMetadataRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataRequest.md)
- [SubscriptionChangeMetadataResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataResponse.md)
- [SubscriptionChangeMetadataDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataDescriptors.md)
- [SubscriptionChangeMetadataItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataItem.md)

---


## changeitemnotfounderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ChangeItemNotFoundError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## changelog

## 

Use this changelog to learn about feature updates, deprecations, and removals for the Advanced Commerce API.

## 

- Added the `dependentSKUs` field to the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint payload for managing subscription price changes. For more information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/handling-subscription-price-changes](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/handling-subscription-price-changes).
- Added the following error codes: [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/InvalidPriceForChangeItemInPriceIncreaseError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/InvalidPriceForChangeItemInPriceIncreaseError), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/InvalidSKUProvidedMustBeCurrentSKUSetToRenewError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/InvalidSKUProvidedMustBeCurrentSKUSetToRenewError), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/ItemCannotBeSpecifiedMultipleTimesError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/ItemCannotBeSpecifiedMultipleTimesError), and [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError).

## 

Added support for the [https://developer.apple.com/programs/mini-apps-partner/](https://developer.apple.com/programs/mini-apps-partner/).

## 

Added tax codes for games in [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/taxcodes](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/taxcodes).

## 

- Added the error code [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/TransactionCannotBeRefundedContactSupportError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/TransactionCannotBeRefundedContactSupportError).
- Removed the unused error code `TransactionNotFoundError`.

## 

Added the endpoints [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API), [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund), and [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription), and the related data types and error codes.

## 

Initial release.

## See Also

- [setting-up-your-project-for-advanced-commerce](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce.md)
- [setupmanagesubscriptions](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setupmanagesubscriptions.md)

---


## creating-skus-for-the-mini-app-partner-program

## 

If your app supports the Mini Apps Partner Program, use the Advanced Commerce APIs when a customer initiates a one-time purchase ([doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest)), or purchases a subscription ([doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest)).

The Mini Apps Partner Program has specific requirements for defining the SKUs and the product display names, so they fully identify each mini app product. Follow these guidelines to create display names and SKUs for products you offer through the Mini Apps Partner Program and describe the format for one-time purchases and subscriptions. See [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases) for additional guidance.

## 

The following table lists the identifiers that make up mini app display names and SKUs.

| Identifier | Description | Example |
| --- | --- | --- |
| `[Mini App Name]` | The name of the mini app | `Anne’s Game` |
| `[Mini App Product Name]` | The name of the product associated with the mini app | `Boost Pack` or `Pro Monthly` |
| `[Mini App Partner Name]` | The name of the mini app partner | `Apple_Seed` |
| `[Mini App Partner ID]` | The unique identifier you set for the mini app partner | `WC123` |
| `[Mini App SKU Identifier]` | The unique identifier you set for the Mini App Product | `boost_pack_id, pro_monthly_id` |

You determine the names and concatenate them to create the display names and SKUs, as specified in the one-time or subscription purchase instructions below, when you use the Advanced Commerce APIs to initiate purchases.

## 

To initiate a one-time charge for a mini app product, use the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest).

Create the mini app display name using the format `[Mini App Name] - [Mini App Product Name]`. Using the sample values from the table above, `item.displayName` would look like the following example:

```None
item.displayName = "Anne’s Game - Boost Pack"
```

- The display name can use a maximum of 30 characters.
- The two elements are separated by the ‘-’ character, with a single space on either side of the ‘-’ character.

Create the `item.SKU` using the format `[Mini App SKU Identifier]|[Mini App Partner Name]|[Mini App Partner ID]`

Using the sample values from the table above, the `items.SKU` would look like the following example:

```None
item.SKU = "boost_pack_id |Apple_Seed|WC123"
```

- The SKU value needs to be unique within your app and can use a maximum of 128 characters.
- All three elements are separated by the ‘|’ character and all three elements must be present.

## 

To initiate a subscription purchase, use the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest) API.

Create the display name and SKU in [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateItem](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateItem) to include the specified details and ensure it conforms to the indicated formatting and length limitations.

The mini app’s display name can use a maximum of 30 characters, and follows this format: `descriptors.displayName` = `[Mini App Name]`, for example

```None
descriptors.displayName = "Anne's Game"
```

The product display name can use a maximum of 30 characters and follow this format: `items.displayName` = `[Mini App Product Name]`, for example

```None
items.displayName = "Pro Monthly"
```

The SKU value needs to be unique within your app and can use a maximum of 128 characters and follows this format: items.SKU = `[Mini App SKU Identifier]|[Mini App Partner Name]|[Mini App Partner ID]`, for example

```None
items.SKU = "pro_monthly_id|Apple_Seed|WC123"
```

All three elements are separated by the ‘|’ character and all three elements must be present.

## See Also

- [setting-up-generic-product-identifiers](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setting-up-generic-product-identifiers.md)
- [creating-your-purchases](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/creating-your-purchases.md)

---


## creating-your-purchases

## 

For each purchase you plan to offer, create a product identifier, or SKU, in your system along with corresponding text such as display name and price. The App Store displays this information on the payment sheet when a customer initiates a purchase, which helps them understand the transaction before they confirm their purchase. The App Store also uses this information in additional communication to the customer, including in email receipts and in the Apple Account Settings under Subscriptions.

To ensure your purchases display properly and provide a quality experience, follow these guidelines:

- Be clear, concise, and descriptive.
- Use proper capitalization and punctuation, and avoid using all capitals.
- Create localized information for any regions where your app is available.
- Consider how you use special characters (for example, hyphens, periods, and underscores) and diacritics. You can use special characters, but avoid using them excessively or beginning strings with them.
- Don’t use markup language, emoticons, diacritics, or control characters (for example, null, new lines, carriage returns, escape, or other invisible characters) that cause strings to exceed a single line.

Review the Human Interface Guidelines for additional best practices for [https://developer.apple.com/design/human-interface-guidelines/writing](https://developer.apple.com/design/human-interface-guidelines/writing) and designing your [https://developer.apple.com/design/human-interface-guidelines/in-app-purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase). If you offer subscriptions, get additional best practices for [https://developer.apple.com/app-store/subscriptions/#clear-description](https://developer.apple.com/app-store/subscriptions/#clear-description) in your paywalls and payment sheets.

## 

Manage one-time purchases — such as one-time rentals, books, or courses — by using the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest) API to provide information to the App Store when the customer initiates a purchase. After a one-time charge is complete, customers receive an email receipt from Apple.



The following details appear in the App Store payment sheet as well as your email receipt; you set both of these values in the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeItem](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeItem) of the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest):

- item.[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName): The name of the item the customer is purchasing.
- item.[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price): The price of the item the customer is purchasing.



> **NOTE:** You can set up an image that displays in the payment sheet instead of the app icon. For more information, see the “Set up an image for the payment sheet to display” section in [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce).

## 

Use the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest) API to provide information to the App Store when the customer initiates a purchase for each subscription SKU you offer. After a successful purchase, Apple sends customers a subscription confirmation email and a receipt. Customers can go to their Apple Account Subscription Settings to manage their subscription at any time.



The following details appear in the App Store payment sheet, email communications from Apple, and the customer’s Apple Account Subscription Settings; you set the values of these details in [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest):

- [https://developer.apple.com/documentation/advancedcommerceapi/Descriptors](https://developer.apple.com/documentation/advancedcommerceapi/Descriptors).[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName): The name of the subscription the customer is purchasing.
- [https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem](https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName): The tier of the subscription service the customer is purchasing, which needs to be different from your `descriptors.displayName`. For example, if your app includes creator subscriptions and a creator offers multiple subscription tiers, the `displayName` represents the tier the customer is purchasing.
- [https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem](https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price): The price of the item the customer is purchasing.
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/period](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/period): The duration of the subscription’s billing cycle.
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/currency](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/currency): The currency that your app uses to charge the customer.
- App link: A dedicated link for customers to manage their subscription within your app. This link appears in the customer’s Apple Account Subscription Settings as a “Manage in [Your App Name]” button. For setup information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setupmanagesubscriptions](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setupmanagesubscriptions). You must also provide a way for customers to [https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest) to a subscription that has expired or has automatic renewals turned off.



## 

For subscription-specific services that are bundled with additional add-on content or services (all of which auto-renews as a single subscription), create a SKU for each service or content offering. Use the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest) API to provide information to the App Store when the customer initiates a purchase. After a successful purchase, Apple sends customers a subscription confirmation email and a receipt. Customers can go to their Apple Account Subscription Settings to manage their subscription at any time.



The following details appear in the App Store payment sheet, email communications from Apple, and customer’s Subscription Settings; you set the values of these details in [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest):

- [https://developer.apple.com/documentation/advancedcommerceapi/Descriptors](https://developer.apple.com/documentation/advancedcommerceapi/Descriptors).[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName): The name of the subscription SKU a customer is purchasing. This needs to represent your overall subscription as well as be relevant for any combination of SKUs someone might choose to bundle.
- [https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem](https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/displayName): The name of the add-on a customer is purchasing. For example, for a streaming app with multiple channel add-ons, this string might be “Live Sports”.
- [https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem](https://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price): The price for each add-on within the bundled subscription purchase. When your app or email displays multiple bundle items, it sorts them from highest to lowest price.
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/period](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/period): The duration of the subscription’s billing cycle.
- [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/currency](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/currency): The currency that your app uses to charge the customer.
- App link: A dedicated link for customers to manage their subscription within your app. This link appears in the customer’s Apple Account Subscription Settings as a “Manage in [Your App Name]” button. For setup information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setupmanagesubscriptions](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setupmanagesubscriptions). You must also provide a way for customers to [https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest) to a subscription that has expired or has automatic renewals turned off.



## See Also

- [setting-up-generic-product-identifiers](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setting-up-generic-product-identifiers.md)
- [creating-skus-for-the-mini-app-partner-program](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/creating-skus-for-the-mini-app-partner-program.md)

---


## currency

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string currency
```

## 

The currency property contains an ISO 4217 alpha-3 string that represents the currency of the price of a SKU. You provide a currency value each time you create or modify a purchase transaction.

To get the current storefront’s currency in your app:

- In iOS 15 through iOS 17, check the `Product.priceFormatStyle.currencyCode` of the generic product ID that represents your Advanced Commerce product. For more information, see [doc://com.apple.documentation/documentation/StoreKit/Product/priceFormatStyle](doc://com.apple.documentation/documentation/StoreKit/Product/priceFormatStyle).
- In iOS 17 and later, get the currency value using `Storefront.current.currency`.

For a list of regions and currencies that the App Store supports, see [https://developer.apple.com/help/app-store-connect/reference/financial-report-regions-and-currencies](https://developer.apple.com/help/app-store-connect/reference/financial-report-regions-and-currencies).

## See Also

- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## currentskulengthexceedederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object CurrentSKULengthExceededError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## datatypes

## Topics

### Objects

- [Descriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Descriptors.md)
- [Offer](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Offer.md)
- [RequestInfo](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestInfo.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyDescriptors.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionPriceChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeItem.md)

### Data types

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)
- [transactionId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/transactionId.md)
- [version](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/version.md)

---


## dependentSKU

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string dependentSKU
```

### 

A dependent SKU is a product identifier that represents an item that depends on another SKU in the context of subscription price changes. Dependent SKUs cannot be chained or shared between multiple parent SKUs.

The dependentSKU value is a string with a maximum length of 128 characters.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## dependentskuscannotbechainederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object DependentSKUsCannotBeChainedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## dependentskuscannotbesharederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object DependentSKUsCannotBeSharedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## description

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string description
```

## 

You provide a description of a SKU when you create or modify a purchase transaction. You can use this description for your own purpose; it isn’t displayed to customers or used for any purpose by the API.

> **IMPORTANT:** Don’t include any personal customer information in the description.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## displayName

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string displayName
```

## 

You provide a display name for every SKU you offer in your app. For subscriptions, provide clear, distinguishable subscription options. Use short, self-explanatory names that differentiate subscription options from one another.

You can provide localized display names, based on the customer’s storefront. For more information on storefronts, see [doc://com.apple.documentation/documentation/StoreKit/Storefront](doc://com.apple.documentation/documentation/StoreKit/Storefront).

For more information and best practices on providing names and other data the system displays to customers, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases).

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## effective

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string effective
```

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## emptyaddchangeitemserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object EmptyAddChangeItemsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## errorcodes

## Topics

### Error codes

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)
- [InvalidAmountError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidAmountError.md)
- [InvalidAppAccountTokenError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidAppAccountTokenError.md)
- [InvalidChangeReasonError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidChangeReasonError.md)
- [InvalidConsistencyTokenError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidConsistencyTokenError.md)
- [InvalidCurrencyError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidCurrencyError.md)
- [InvalidDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidDescriptionError.md)
- [InvalidDisplayNameError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidDisplayNameError.md)
- [InvalidOfferPeriodCountError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidOfferPeriodCountError.md)
- [InvalidOfferPeriodError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidOfferPeriodError.md)
- [InvalidOfferPriceError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidOfferPriceError.md)
- [InvalidOfferReasonError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidOfferReasonError.md)
- [InvalidOperationError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidOperationError.md)
- [InvalidPreviousSubscriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidPreviousSubscriptionError.md)
- [InvalidPreviousTransactionIDError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidPreviousTransactionIDError.md)
- [InvalidPriceForChangeItemInPriceIncreaseError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidPriceForChangeItemInPriceIncreaseError.md)
- [InvalidProductChangesError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidProductChangesError.md)
- [InvalidProductError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidProductError.md)
- [InvalidProratedPriceError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidProratedPriceError.md)
- [InvalidRefundReasonError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidRefundReasonError.md)
- [InvalidRefundTypeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidRefundTypeError.md)
- [InvalidRenewalPeriodError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidRenewalPeriodError.md)
- [InvalidRenewalPriceError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidRenewalPriceError.md)
- [InvalidRequestReferenceIDError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidRequestReferenceIDError.md)
- [InvalidSalableDurationError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidSalableDurationError.md)
- [InvalidSalableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidSalableError.md)
- [InvalidSignatureError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidSignatureError.md)
- [InvalidSKUError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidSKUError.md)
- [InvalidSKUProvidedMustBeCurrentSKUSetToRenewError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidSKUProvidedMustBeCurrentSKUSetToRenewError.md)
- [InvalidStorefrontError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidStorefrontError.md)
- [InvalidTargetProductIDError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidTargetProductIDError.md)
- [InvalidTaxProductCodeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidTaxProductCodeError.md)
- [InvalidTransactionIdError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InvalidTransactionIdError.md)
- [ItemCannotBeSpecifiedMultipleTimesError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ItemCannotBeSpecifiedMultipleTimesError.md)
- [ItemLimitExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ItemLimitExceededError.md)
- [MalformedPayloadError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MalformedPayloadError.md)
- [MisalignedBillingCycleError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MisalignedBillingCycleError.md)
- [MismatchedStorefrontError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MismatchedStorefrontError.md)
- [MissingPricingConfigForStorefrontError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MissingPricingConfigForStorefrontError.md)
- [MissingUpdatedItemsWithPeriodChangeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MissingUpdatedItemsWithPeriodChangeError.md)
- [MoreItemsThanAllowedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MoreItemsThanAllowedError.md)
- [MoreOffersThanAllowedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MoreOffersThanAllowedError.md)
- [MultipleOperationsOnSingleSKUError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MultipleOperationsOnSingleSKUError.md)
- [MultiplePricesError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/MultiplePricesError.md)
- [NegativePriceError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NegativePriceError.md)
- [NegativeProratedPriceError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NegativeProratedPriceError.md)
- [NegativeRefundAmountError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NegativeRefundAmountError.md)
- [NullAdvancedCommerceDataError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullAdvancedCommerceDataError.md)
- [NullCurrencyError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullCurrencyError.md)
- [NullCurrentSKUError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullCurrentSKUError.md)
- [NullDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullDescriptionError.md)
- [NullDescriptorsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullDescriptorsError.md)
- [NullDisplayNameError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullDisplayNameError.md)
- [NullEffectiveError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullEffectiveError.md)
- [NullItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullItemError.md)
- [NullItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullItemsError.md)
- [NullNewSKUError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullNewSKUError.md)
- [NullOfferPeriodError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullOfferPeriodError.md)
- [NullPeriodCountError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullPeriodCountError.md)
- [NullPeriodError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullPeriodError.md)
- [NullPriceError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullPriceError.md)
- [NullReasonError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullReasonError.md)
- [NullRefundAmountError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRefundAmountError.md)
- [NullRefundReasonError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRefundReasonError.md)
- [NullRefundRiskingError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRefundRiskingError.md)
- [NullRefundTypeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRefundTypeError.md)
- [NullRequestInfoError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRequestInfoError.md)
- [NullRequestReferenceIDError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRequestReferenceIDError.md)
- [NullRetainBillingCycleError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullRetainBillingCycleError.md)
- [NullSKUError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullSKUError.md)
- [NullStorefrontError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullStorefrontError.md)
- [NullTargetProductIDError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullTargetProductIDError.md)
- [NullTaxCodeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullTaxCodeError.md)
- [NullTransactionIdError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullTransactionIdError.md)
- [NullVersionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/NullVersionError.md)
- [OfferPreventsItemMidCycleChangeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OfferPreventsItemMidCycleChangeError.md)
- [OneItemNeededInModifyError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OneItemNeededInModifyError.md)
- [OperationNotAllowedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OperationNotAllowedError.md)
- [PartialSimulateRefundDeclineError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PartialSimulateRefundDeclineError.md)
- [PendingChangesMismatchError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PendingChangesMismatchError.md)
- [PendingRefundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PendingRefundError.md)
- [PeriodChangeEffectiveConflictError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PeriodChangeEffectiveConflictError.md)
- [PeriodChangeImmediateWithEffectiveAtNextBillingCycleError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PeriodChangeImmediateWithEffectiveAtNextBillingCycleError.md)
- [PeriodCountNotPositiveError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PeriodCountNotPositiveError.md)
- [PeriodResetWithRetainBillingCycleError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PeriodResetWithRetainBillingCycleError.md)
- [PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError.md)
- [PriceChangeNotSupportedThroughModifyItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/PriceChangeNotSupportedThroughModifyItemsError.md)
- [ProductAlreadyExistsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ProductAlreadyExistsError.md)
- [ProductNotEligibleError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ProductNotEligibleError.md)
- [ProductNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ProductNotFoundError.md)
- [ProductNotOwnedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ProductNotOwnedError.md)
- [ProratedOnlyLatestTransactionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ProratedOnlyLatestTransactionError.md)
- [RateLimitExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RateLimitExceededError.md)
- [RefundAmountWithoutCustomError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RefundAmountWithoutCustomError.md)
- [RemovalAllNotAllowedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RemovalAllNotAllowedError.md)
- [RemoveAllItemsNotAllowedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RemoveAllItemsNotAllowedError.md)
- [RemoveItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RemoveItemNotFoundError.md)
- [RemoveItemsWithoutAddOrChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RemoveItemsWithoutAddOrChangeItemsError.md)
- [RepeatedRequestReferenceIdError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RepeatedRequestReferenceIdError.md)
- [RevokeOnInactiveSubscriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RevokeOnInactiveSubscriptionError.md)
- [SimulateRefundDeclineOnlyInSandboxError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SimulateRefundDeclineOnlyInSandboxError.md)
- [SKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKULengthExceededError.md)
- [StorefrontChangeError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/StorefrontChangeError.md)
- [SubscriptionAlreadyActiveError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionAlreadyActiveError.md)
- [SubscriptionAlreadyExistsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionAlreadyExistsError.md)
- [SubscriptionAlreadyMigratedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionAlreadyMigratedError.md)
- [SubscriptionDoesNotExistError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionDoesNotExistError.md)
- [SubscriptionNotEligibleError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionNotEligibleError.md)
- [TransactionIdNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/TransactionIdNotFoundError.md)
- [TransactionNotRefundableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/TransactionNotRefundableError.md)
- [TransactionCannotBeRefundedContactSupportError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/TransactionCannotBeRefundedContactSupportError.md)
- [UnauthorizedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/UnauthorizedError.md)
- [UnexpectedVersionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/UnexpectedVersionError.md)

---


## generalinternalerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object GeneralInternalError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## handling-subscription-price-changes

## 

The Advanced Commerce API provides a standard UI to facilitate price increases for subscriptions and manage the subscriber consent process.

> **NOTE:** The AppStore doesn’t currently support the Advanced Commerce price increase mechanism in India.

## 

Use the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint in the Advanced Commerce API (ACA) to initiate a price change for an individual subscription item. The UI the framework provides manages all of the necessary interactions and communication with a person using your app, including:

- Consent management for price increases.
- Notifications about price increases when the price increase doesn’t requite explicit consent.
- A standard UI sheet that App Store displays to obtain explicit user consent, if required, or an acknowledgment of the price increase if explicit consent isn’t required. Examples of these sheets and an explanation of the information they display about your app and the subscription are shown below.





## 

The App Store checks if a price increase requires consent, and follows different paths depending on whether a subscriber needs to explicitly consent to a price increase or not.

### 

The App Store requests explicit consent from the subscriber if the price increase meets any of the following criteria:

- The subscriber is located in a region that requires consent for any price changes. For more information about these regions, see [https://help.apple.com/app-store-connect/#/devf3e625675](https://help.apple.com/app-store-connect/#/devf3e625675).
- The price increase is: - More than 50 percent of the current price; and
- The difference in price exceeds 5 United States Dollars (USD) per period for nonannual subscriptions, or 50 USD per year for annual subscriptions. International equivalents for prices not in USD are based on current exchange rates with specific thresholds subject to change based on changes in taxes or foreign exchange rates.
- The subscriber had a price increase for the same subscription within the past 12 months.
- The subscriber is located in South Korea and is converting from a free trial to a paid subscription, or from a discounted offer to a standard subscription price. For subscribers in South Korea, see [#Implement-communication-and-consent-management-for-South-Korea](#Implement-communication-and-consent-management-for-South-Korea) at the end of this article.

When conditions require consent, the App Store notifies subscribers via email, price increase sheet, and push notification, according to the timelines below. If a subscriber doesn’t take any action, the App Store continues to request consent no more than once per week for each method. You can’t raise the price until you receive the subscriber’s consent.

The following notification timeline applies to all cases, except for subscribers in South Korea who are converting from free trials and discount offers:

| Subscription interval | Email, price increase sheet, and push notification timelines |
| --- | --- |
| For 2-month, 3-month, 6-month, and annual subscriptions | 60 days before the renewal date |
| Monthly subscriptions | 27 days before the renewal date |
| Weekly subscriptions | 7 days before the renewal date |



### 

When a price increase doesn’t need the subscriber’s consent, the App Store only notifies subscribers about the new price. When the App Store increases the price of multiple items within a bundle, none of which require consent, it uses a single API request so the subscriber receives a summary of the price increases. The App Store combines notifications into a single communication per method (a single email, one price increase sheet, and a single push notification).

The App Store uses the following communications methods and timelines to notify subscribers:

> **NOTE:** Unlike when requesting consent, the App Store doesn’t send a push notification if the subscriber acknowledges the price increase on the sheet. Notifying via email is still a requirement in either case.

## 

Several conditions may affect your ability to change or update a subscription, including:

- During the price increase window, the renewal uses the increased price that the developer has specified  using [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) if you make any of the following changes to the subscription: - Adding an item
- Removing an item
- Changing an item
- Resubscribing using the [https://developer.apple.com/documentation/advancedcommerceapi#Subscription-modification-in-the-app](https://developer.apple.com/documentation/advancedcommerceapi#Subscription-modification-in-the-app)  or the [com.apple.documentation/documentation/advancedcommerceapi#Subscription-reactivation-in-the-app](com.apple.documentation/documentation/advancedcommerceapi#Subscription-reactivation-in-the-app)
- If the subscription status is auto-renew = `false` or if the subscription is in a grace period or billing retry state, you can’t call the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint.
- If the `SubscriptionPriceChangeItem` is currently in the offer period, you can’t call [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price).

## 

Several conditions can affect your ability to update a subscription. There may be specific interactions and rules that apply to price increases, depending on which Advanced Commerce API you need to use.

If you need to reactivate items, call the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest) API. The following conditions apply to reactivations:

- If the App Store communicated the price increase, it reactivates the items you provide through the `items` key in the properties you supply to the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest) request at the higher price. Failing to explicitly reactivate an item doesn’t result in the App Store activating the higher price, because the App Store needs to communicate the price increase and receive consent through the normal process.
- If the App Store hasn’t communicated the price increase, it schedules the price increase communications for the next eligible date.

If you need to  modify a subscription, call the  [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionModifyInAppRequest](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionModifyInAppRequest) API. Price increases interact with the ACA in a specific way depending on if the call resets or retains the billing cycle.

If the price increase will take place during a retain billing cycle, the following rules apply:

- If the App Store communicated the price increase: - If the price increase is pending consent, the higher price is shown in the Payment Sheet, and the user must consent to the price increase via the in-app sheet that appears, or via Manage Subscriptions.
- If the subscriber consented to the  price increase, or the price increase doesn’t require consent,  the Payment Sheet shows the higher price.
- If the  subscriber declined the price increase, the item doesn’t appear in the Payment Sheet.
- If the item’s SKU is changing to a different product SKU (such as from SKU `BASIC` to SKU `PREMIUM`), the change invalidates the price increase, since the new SKU represents a different product.
- When the App Store sends an offer with an item subject to a price increase, it’s a *special consideration*; in this case, you send the higher price of the item, and the App Store reschedules the price increase for after the offer period has completed, at which point, the item renews at the higher price.

If the price increase will take place during a reset billing cycle, the following rules apply:

- If the App Store hasn’t communicated the  price increase, the price increase is invalidated.
- If the the App Store communicated the price increase, the App Store applies the new price only if the item is sent with the higher price, using the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionModifyChangeItem](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionModifyChangeItem). - As described above, changing the item to a different product (such as changing from *BASIC* SKU  to a *Premium* SKU) invalidates the price increase, as the item represents a different product.

If you need to change a subscription’s metadata, call the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata). Metadata-only changes, such as changing the SKU from SKU A to SKU B, preserves the price increase because it isn’t a change in product, but rather a change to the product SKU.

If you need to call the ACA Migration API to migrate a subscription that a subscriber purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API, the following rules apply:

- If the In-App purchase product has a pending price increase through App Store Connect, the App Store doesn’t allow the migration if it has already communicated the price increase to the subscriber.
- The App Store doesn’t allow migrations if the item is currently subject to a price increase, and the App Store already sent price increase communications to the subscriber.
- If there’s an upcoming price increase, the App Store migrates the pending price increase as well.

## 

The following table describes the meaning of prince increase status values:

| Price increase info status | Description |
| --- | --- |
| `priceIncreaseInfo.SCHEDULED` | Indicates the App Store scheduled the price increase for the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionPriceChangeItem](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionPriceChangeItem). |
| `priceIncreaseInfo.PENDING` | Indicates there’s a pending price increase for the `SubscriptionPriceChangeItem` that requires subscriber consent, and the subscriber hasn’t yet consented. If the subscriber doesn’t consent, the `SubscriptionPriceChangeItem` expires at the end of the billing cycle. |
| `priceIncreaseInfo.ACCEPTED` | Indicates that the subscriber consented to a price increase for the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionPriceChangeItem](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/SubscriptionPriceChangeItem). |

The following table describes the notifications and status values for a subscription price change item that requires consent:

| Notification type | Subtype | Property details | Description |
| --- | --- | --- | --- |
| `PRICE_CHANGE` | - | `priceIncreaseInfo.SCHEDULED` | Indicates that you called the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price)  endpoint. This notification only applies to apps that use the Advanced Commerce API. |
| `PRICE_INCREASE` | `PENDING` | `priceIncreaseInfo.PENDING` | Indicates there’s a pending price increase for the SKU that requires subscriber consent, and the subscriber hasn’t yet consented. If the subscriber doesn’t consent, the SKU expires at the end of the billing cycle. |
| `PRICE_INCREASE` | `ACCEPTED` | `priceIncreaseInfo.ACCEPTED` | Indicates that the subscriber consented to a price increase for the SKU. |
| `EXPIRED` | `PRICE_INCREASE` | - | Indicates that the auto-renewable subscription expired because the subscriber didn’t consent to the price increase, and allowed the subscription to expire. |
| `EXPIRED` | `VOLUNTARY` | - | Indicates that the subscriber voluntarily canceled the auto-renewable subscription. This notification type and subtype isn’t specific to price increases. |
| `DID_RENEW` | - | - | Indicates the SKU renewed. Always check  [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSRenewalInfo](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSRenewalInfo) and the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSTransaction](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSTransaction) information to provide service to the list items. |

The following table describes the notifications and status values for a subscription price change item that doesn’t require consent:

| Notification type | Subtype | Property details | Description |
| --- | --- | --- | --- |
| `PRICE_CHANGE` | - | `priceIncreaseInfo.SCHEDULED` | Indicates that you called the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint. This notification only applies to apps that use the Advanced Commerce API. |
| `PRICE_INCREASE` | `ACCEPTED` | `priceIncreaseInfo.ACCEPTED` | Indicates that the App Store informed the subscriber for the subscription price increase for the item, and it is subject to the price increase. |
| `EXPIRED` | `VOLUNTARY` | - | Indicates that the subscriber voluntarily canceled the auto-renewable subscription. This notification type and subtype isn’t specific to price increases. |
| `DID_RENEW` | - | - | The SKU renewed. Always check  [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSRenewalInfo](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSRenewalInfo) and the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSTransaction](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSTransaction) information to provide service to the list items. |

The following table describes the notifications and status values for a subscription price change item that decreases a price:

| Notification type | Subtype | Property details | Description |
| --- | --- | --- | --- |
| `PRICE_CHANGE` | - | - | Indicates that you called the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint. This notification only applies to apps that use the Advanced Commerce API. |
| `DID_RENEW` | - | - | Indicates the SKU renewed. Always to check to ensure [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSRenewalInfo](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSRenewalInfo) and the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSTransaction](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/JWSTransaction) information to provide service to the list items. |

## 

To create a contingency for a situation in which a person doesn’t agree to a price increase and the App Store cancels other, bundled services (the “dependent SKUs”), you can provide an array of the SKUs through the `dependentSKUs` property. If the price increase requires a person’s consent, and they don’t consent to the price increase (through a cancellation from the Manage Subscriptions view, or by failing to consent before the renewal date), the App Store cancels the dependent SKUs.

> **IMPORTANT:** You can’t have chains of dependent SKUs –– for example, if SKU *A* has dependent SKU *B*, *B* can’t have its own dependent SKU, *C*. However, *B* can have its own price increase.

## 

To test subscription price increases, call the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) API in the sandbox to test the API responses. The sandbox environment — and TestFlight — support the full price increase cycle, with the exception of the email and push notifications. The in-app sheet still appears, and price increase management appears on the Manage Subscriptions page.

You can test granting consent or declining a price increase through the in-app sheet or by navigating to the Manage Subscription page in the sandbox. For more information, see [doc://com.apple.documentation/documentation/StoreKit/testing-disabling-auto-renew](doc://com.apple.documentation/documentation/StoreKit/testing-disabling-auto-renew).

In the sandbox, the first renewal after calling [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) uses the existing price to assist in testing states prior to when the App Store communicated the price increase. After the first renewal, the App Store simulates communicating the price increase for the next appropriate renewal.

> **NOTE:** After you call the [doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.documentation/documentation/AdvancedCommerceAPI/Change-Subscription-Price) API, the subscription renews on the higher price after one renewal, giving you time to test in the sandbox environment,

## 

For subscribers in South Korea who convert from a free trial to a paid subscription, or from a discounted offer to a standard subscription price, use the following notification timelines:

| Subscription interval | Email, price increase sheet, and push notification timelines for South Korea |
| --- | --- |
| For 2-month, 3-month, 6-month, and annual subscriptions | Within 30 days from the day before the payment or conversion |
| Monthly subscriptions | Within 30 days from the day before the payment or conversion |
| Weekly subscriptions | Within 30 days from the day before the payment or conversion |

> **NOTE:** For free trial or discounted offer conversions in South Korea, the 30-day window for notifications doesn’t include the conversion or payment date. For example, if a two-month free trial starts on March 1 and the payment or conversion date is May 1, you’re required to obtain the consent from the person between April 1 and April 30, the 30-day window before the payment or conversion date.

## See Also

- [prices](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/prices.md)
- [taxcodes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxcodes.md)

---


## inactiveacasuberror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InactiveACASubError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InsufficientFundsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InsufficientFundsError.md)

---


## insufficientfundserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InsufficientFundsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidappaccounttokenerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidAppAccountTokenError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidchangereasonerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidChangeReasonError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidconsistencytokenerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidConsistencyTokenError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidofferperioderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidOfferPeriodError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidofferpriceerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidOfferPriceError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidofferreasonerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidOfferReasonError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidoperationerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidOperationError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidprevioustransactioniderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidPreviousTransactionIDError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidpriceforchangeiteminpriceincreaseerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidPriceForChangeItemInPriceIncreaseError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidproductchangeserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidProductChangesError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidproratedpriceerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidProratedPriceError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidrefundtypeerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidRefundTypeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidrenewalpriceerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidRenewalPriceError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidrequestreferenceiderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidRequestReferenceIDError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidsignatureerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidSignatureError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidstorefronterror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidStorefrontError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidtaxproductcodeerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidTaxProductCodeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## invalidtransactioniderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object InvalidTransactionIdError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## jwsrenewalinfo

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string JWSRenewalInfo
```

### 

This `JWSRenewalInfo` object is identical to the one used in the App Store Server API and by App Store Server Notifications. For details, see [doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSRenewalInfo](doc://com.apple.documentation/documentation/AppStoreServerAPI/JWSRenewalInfo).

## See Also

- [JWSTransaction](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/JWSTransaction.md)

---


## misalignedbillingcycleerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MisalignedBillingCycleError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## mismatchedstorefronterror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MismatchedStorefrontError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## moreoffersthanallowederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MoreOffersThanAllowedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## multipleoperationsonsingleskuerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MultipleOperationsOnSingleSKUError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## multiplepriceserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object MultiplePricesError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## negativepriceerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NegativePriceError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullcurrencyerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullCurrencyError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullcurrentskuerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullCurrentSKUError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nulldescriptionerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullDescriptionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nulldescriptorserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullDescriptorsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nulleffectiveerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullEffectiveError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullperioderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullPeriodError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullrefundreasonerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRefundReasonError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullrefundtypeerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRefundTypeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullrequestinfoerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullRequestInfoError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullskuerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullSKUError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullstorefronterror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullStorefrontError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nulltaxcodeerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullTaxCodeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nulltransactioniderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullTransactionIdError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## nullversionerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object NullVersionError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## oneitemneededinmodifyerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object OneItemNeededInModifyError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## onetimechargecreaterequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object OneTimeChargeCreateRequest
```

### 

## See Also

- [OneTimeChargeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/OneTimeChargeItem.md)

---


## operationnotallowederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object OperationNotAllowedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## partialsimulaterefunddeclineerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PartialSimulateRefundDeclineError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## pendingrefunderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PendingRefundError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## period

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string period
```

### 

Auto-renewable subscriptions renew periodically. For example, if the period is 2 months, the subscription renews every 2 months.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## periodchangeimmediatewitheffectiveatnextbillingcycleerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PeriodChangeImmediateWithEffectiveAtNextBillingCycleError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## periodcountnotpositiveerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PeriodCountNotPositiveError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## price

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
int64 price
```

## 

Provide SKU prices using the supported number of decimal places for the currency, in milliunit format. For more information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/prices](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/prices).

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## pricechangecannotbeissuedwhenalreadycommunicatederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## prices

## 

Apps that use the Advanced Commerce API manage their own catalog of in-app purchases and their respective SKUs, including their prices. When supplying a price, be sure to use the supported number of decimal places, as shown in the section below. In the API, provide the price value in milliunit format.

When setting a price for your SKU, it’s strongly recommended that you choose from the 900 price points that the App Store supports across 175 storefronts and 44 currencies. To view or download a .csv file that includes all the storefronts, currencies, and price points:

- In [https://appstoreconnect.apple.com/login](https://appstoreconnect.apple.com/login), log in with an App Manager role.
- Select Apps, and choose your app.
- In the left menu, select Pricing and Availability.
- Select Available Prices by Country or Region.
- Select Download All Prices and Currencies.

For price point information by currency, see [https://www.apple.com/newsroom/pdfs/App-Store-Pricing-Update.pdf](https://www.apple.com/newsroom/pdfs/App-Store-Pricing-Update.pdf).

### 

To determine the currency to use at runtime, check the device’s App Store storefront. For a list of currencies that the App Store supports for each storefront, see [https://developer.apple.com/help/app-store-connect/reference/financial-report-regions-and-currencies](https://developer.apple.com/help/app-store-connect/reference/financial-report-regions-and-currencies). For information about getting the current storefront in the app, see the [doc://com.apple.documentation/documentation/StoreKit/Storefront/current](doc://com.apple.documentation/documentation/StoreKit/Storefront/current) property of [doc://com.apple.documentation/documentation/StoreKit/Storefront](doc://com.apple.documentation/documentation/StoreKit/Storefront). For more information on currency, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/currency](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/currency).

### 

The Advanced Commerce API accepts prices in milliunit format, as noted in the documentation, such as for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/price) type.

To determine a price in milliunits, multiply the price by 1000.  One unit of a currency equals 1000 milliunits. The following table shows examples of valid prices in milliunit format:

| Price | Milliunits |
| --- | --- |
| USD 1.99 | 1990 |
| KRW 3300 | 3300000 |
| JPY 359 | 359000 |

> **NOTE:** The payment sheet and other customer communications automatically display prices in the standard format, not in milliunits.

### 

The App Store supports either zero or two decimal places for prices, depending on the currency.

The following table shows examples of valid and invalid prices, based on the number of decimal places they use:

| Currency | Supported decimal places | Valid price example (and milliunit equivalent) | Invalid price example (and milliunit equivalent ) |
| --- | --- | --- | --- |
| USD | 2 | 1.45 (1450) | $1.095  (1095) |
| JPY | 0 | 310  (310000) | 310.95  (310950) |

> **IMPORTANT:** Don’t exceed the supported number of decimal places when you supply a price in the Advanced Commerce API. If your API call includes more decimal digits on a price than its currency supports, the system doesn’t display the payment sheet and fails with an error.

### 

The following currencies don’t support any decimal places:

| Currency code | Decimal places |
| --- | --- |
| CLP | 0 |
| COP | 0 |
| DKK | 0 |
| HKD | 0 |
| HUF | 0 |
| IDR | 0 |
| INR | 0 |
| JPY | 0 |
| KRW | 0 |
| KZT | 0 |
| MXN | 0 |
| NGN | 0 |
| NOK | 0 |
| PHP | 0 |
| PKR | 0 |
| RUB | 0 |
| SEK | 0 |
| THB | 0 |
| TWD | 0 |
| TZS | 0 |
| VND | 0 |

The following currencies support two decimal places:

| Currency code | Decimal places |
| --- | --- |
| AED | 2 |
| AUD | 2 |
| BGN | 2 |
| BRL | 2 |
| CAD | 2 |
| CHF | 2 |
| CNY | 2 |
| CZK | 2 |
| EGP | 2 |
| EUR | 2 |
| GBP | 2 |
| ILS | 2 |
| MYR | 2 |
| NZD | 2 |
| PEN | 2 |
| PLN | 2 |
| QAR | 2 |
| RON | 2 |
| SAR | 2 |
| SGD | 2 |
| TRY | 2 |
| USD | 2 |
| ZAR | 2 |

## See Also

- [taxcodes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxcodes.md)
- [handling-subscription-price-changes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/handling-subscription-price-changes.md)

---


## productalreadyexistserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ProductAlreadyExistsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## productnoteligibleerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ProductNotEligibleError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## productnotfounderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object ProductNotFoundError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## proratedprice

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
int64 proratedPrice
```

## 

For information about prices, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/prices](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/prices).

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## ratelimitexceedederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RateLimitExceededError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## ratelimits

## 

The Advanced Commerce API limits the number of requests that you can submit to each endpoint within a specified timespan. The request limits apply per app. The following table lists the rate limits in the production environment, expressed in requests per second. Limits are enforced on an hourly basis.

| Endpoint | Rate limit (per second) |
| --- | --- |
| [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription) | 5 |
| [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata) | 50 |
| [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price) | 50 |
| [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API) | 50 |
| [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund) | 5 |
| [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription) | 5 |

The rate limits in the sandbox environment are 10 percent of the limits in the table above. The Advanced Commerce server may make adjustments to reduce or increase these rate limits as needed at any time.

### 

If you exceed a per-hour limit, the API rejects the request with an `HTTP 429` response, with a [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/RateLimitExceededError](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/RateLimitExceededError) in the body. Consider the following as you integrate the API:

- If you periodically call the API, throttle your requests to avoid exceeding the per-hour limit for an endpoint.
- Manage the `HTTP 429 RateLimitExceededError` in your error-handling process. For example, log the failure and queue the job to process it again at a later time.
- Check the `Retry-After` header if you receive the `HTTP 429` error. This header contains a UNIX time, in milliseconds, that informs you when you can next send a request.

## See Also

- [authorizing-server-calls](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/authorizing-server-calls.md)

---


## refundAmount

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
integer refundAmount
```

## 

When you supply a requested refund amount, include the tax for all regions, except for Canada and the United States.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## refundReason

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string refundReason
```

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## refundRiskingPreference

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
boolean refundRiskingPreference
```

## 

The App Store uses a variety of factors to determine if a refund request is approved or denied. Set this value to `true` to enable the App Store to ask for consumption information about the product with the refund request. When this value is `true`, you receive a `CONSUMPTION_REQUEST` [doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType](doc://com.apple.documentation/documentation/AppStoreServerNotifications/notificationType) on your your [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint. Respond to the consumption request using the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Send-Consumption-Information](doc://com.apple.documentation/documentation/AppStoreServerAPI/Send-Consumption-Information) to provide additional information that informs and improves the refund process.

Set this value to `false` otherwise. You won’t receive a `CONSUMPTION_REQUEST` notification.

The default value is `true`.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## refundamountwithoutcustomerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RefundAmountWithoutCustomError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## removalallnotallowederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RemovalAllNotAllowedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## removeallitemsnotallowederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RemoveAllItemsNotAllowedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## removeitemnotfounderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RemoveItemNotFoundError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## requestrefunditem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RequestRefundItem
```

## See Also

- [Request-Transaction-Refund](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Request-Transaction-Refund.md)
- [RequestRefundRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundRequest.md)
- [RequestRefundResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundResponse.md)

---


## requestrefundrequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RequestRefundRequest
```

## 

This is the request body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund) endpoint.

## See Also

- [Request-Transaction-Refund](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Request-Transaction-Refund.md)
- [RequestRefundResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundResponse.md)
- [RequestRefundItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundItem.md)

---


## requestrefundresponse

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object RequestRefundResponse
```

## 

##Discussion This is the response body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Request-Transaction-Refund) endpoint.

## See Also

- [Request-Transaction-Refund](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Request-Transaction-Refund.md)
- [RequestRefundRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundRequest.md)
- [RequestRefundItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/RequestRefundItem.md)

---


## retainBillingCycle

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
boolean retainBillingCycle
```

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## setting-up-generic-product-identifiers

## 

A generic product ID is an identifier you set up in App Store Connect and use when you call Advanced Commerce APIs.  The generic product IDs tell the API whether your SKU is a one-time purchase or a subscription, and whether it’s a SKU for the Mini Apps Partner Program.

You may need to create up to four generic product IDs, based on the product types your app offers:

- One-time purchases
- Subscriptions
- One-time purchases for the Mini Apps Partner Program
- Subscriptions for the Mini Apps Partner Program

Generic product IDs aren’t the same as the SKUs for products you offer in your app. Generic product IDs only contain placeholder information for prices, localizations, and subscription periods and don’t contain tax information. You provide price, localization, and tax information for each SKU when you call the Advanced Commerce APIs. For more information about SKUs, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases).

> **IMPORTANT:** Send the generic product IDs you create to Apple, using the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

You need one of these roles: Account Holder, Admin, App Manager, Developer, or Marketing in App Store Connect to add and edit product IDs. For more information, see [https://developer.apple.com/help/app-store-connect/reference/role-permissions](https://developer.apple.com/help/app-store-connect/reference/role-permissions).

### 

To offer one-time purchases using Advanced Commerce API, create a generic product ID in App Store Connect, as follows:

1. Sign in to [https://appstoreconnect.apple.com](https://appstoreconnect.apple.com) and select your app.
2. In the sidebar under Monetization, select In-App Purchases and click the add button (+). The Create an In-App Purchase dialog appears.
3. Create the in-app purchase by entering the following: - **Type**: Consumable
- **Reference Name**: Enabled for Advanced Commerce
- **Product ID**: {your app bundle identifier}.aca.generic.consumable. Replace {your app bundle identifier} with your app’s bundle ID.
4. Click Create to open the details page.

On the details page, configure the following settings:

1. **Availability**: Select the App Store countries or regions that your app supports. For more information, see [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases).
2. **Pricing**: Choose your base country or region and select the lowest available price.
3. **Add Localization**: - **Localization**: English (U.S.)
- **Display Name**: Generic Consumable Product
- **Description**: Use the same text as the display name.

### 

To offer one-time purchases within the Mini Apps Partner Program, create a generic product ID following the instructions for one-time purchases as described above, and enter the following values in the respective topics within the Create an In-App Purchase dialog:

- **Reference Name**: Enabled for Mini Apps Partner Program
- **Product ID**: {your app bundle identifier}.aca.mini.consumable

On the details page, enter these values:

- **Display Name**: Mini App Consumable Product
- **Description**: Mini App Consumable Product

### 

To offer subscriptions using Advanced Commerce API, you first need to create a dedicated subscription group, and then create the generic product ID for a subscription.

To create a dedicated subscription group:

1. Sign in to [https://appstoreconnect.apple.com](https://appstoreconnect.apple.com) and select your app.
2. In the sidebar under Monetization, click Subscriptions and click the add button (+).
3. For **Reference Name**, enter Group for Advanced Commerce and click create.

Next, create the generic product ID for subscriptions:

1. Select the subscription group you created.
2. Under Subscriptions, click Create.
3. Configure the subscription as follows: - **Reference Name**: Enabled for Advanced Commerce
- **Product ID**: {your app bundle identifier}.aca.generic.subscription
4. Click Create to open the details page.

On the details page, configure the following settings:

- **Subscription Duration**: 1 month
- **Family Sharing**: Don’t enable.
- **Set Availability**: Select the App Store countries or regions your app supports. For more information, see [https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription).
- **Add Subscription Price**: Choose your base country or region and select the lowest available price.
- **Add Localization**: - **Localization**: English (U.S.)
- **Display Name**: For Advanced Commerce
- **Description**: For Advanced Commerce

### 

To offer subscriptions within the Mini Apps Partner Program, follow the same process to create a dedicated subscription group and subscription as above, but use the following values:

- For the **Reference Name** of the dedicated subscription group, enter Group for Mini Apps Partner Program.
- For the **Reference Name** of the subscription, enter Enabled for Mini Apps Partner Program subscription.
- For the **Product ID** of the subscription, enter {your app bundle identifier}.aca.mini.generic.subscription.
- For the **Display Name** and **Description** of the localization, enter For Mini Apps Partner Program.

## See Also

- [creating-your-purchases](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/creating-your-purchases.md)
- [creating-skus-for-the-mini-app-partner-program](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/creating-skus-for-the-mini-app-partner-program.md)

---


## setting-up-your-project-for-advanced-commerce

## 

This framework enables you to offer a large catalog of one-time purchases, subscriptions, and bundled content while using the App Store commerce system. To request access to the API, see the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page. After your app receives access, complete the setup to start using the API in your app and on your server.

### 

The Advanced Commerce API relies on up to four generic product identifiers that you create in App Store Connect. See [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setting-up-generic-product-identifiers](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setting-up-generic-product-identifiers) to determine which generic product IDs you need, and how to create them. Send the generic product identifiers to Apple using the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

### 

Set up your server to do the following:

- Support Transport Layer Security (TLS) protocol 1.2 or later.
- Receive [doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2](doc://com.apple.documentation/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) to get up-to-date transaction data. For setup information, see [doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).

### 

Create a deep link into your app that opens a page for customers to manage their subscriptions. For more information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setupmanagesubscriptions](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/setupmanagesubscriptions). Send the deep link to Apple using the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

### 

Review the tax codes you use for your SKUs from the list in [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/taxcodes](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/taxcodes). If you need to request additional tax codes, send your request using the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

### 

Define your SKUs using the best practices for naming and design. For more information, and to learn where the system displays the SKU data you provide, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases). For more design guidance, see Human Interface Guidelines > [https://developer.apple.com/design/human-interface-guidelines/in-app-purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase). To define SKUs for the Mini Apps Partner Program, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-skus-for-the-mini-app-partner-program](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-skus-for-the-mini-app-partner-program).

### 

When you implement the Advanced Commerce API in your app and on your server, you can test in the sandbox environment before sending it to App Review. For more information, see [doc://com.apple.documentation/documentation/StoreKit/testing-in-app-purchases-with-sandbox](doc://com.apple.documentation/documentation/StoreKit/testing-in-app-purchases-with-sandbox).

### 

When customers make a purchase, the payment sheet displays your app icon by default. You can optionally provide an image to use instead, in App Store Connect. To set it up, see the [https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information) topic. Set up one image for the generic product ID that represents your subscriptions, and one for the generic product ID that represents your one-time purchases. For more information on the payment sheet and SKU information that the system displays to customers, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases).

## See Also

- [setupmanagesubscriptions](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setupmanagesubscriptions.md)
- [changelog](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/changelog.md)

---


## setupmanagesubscriptions

## 

Customers use the Settings > Apple Account > Subscriptions page in iOS to manage their subscriptions, including upgrading, downgrading, resubscribing, and canceling. When you offer subscriptions through the Advanced Commerce API, the Subscriptions page displays a “Manage in App” button.



You implement a subscription-management page in your app, and create a deep link URL to it that you submit to Apple. The Settings > Apple Account  > Subscriptions page then uses your deep link for the “Manage in App” button.

> **IMPORTANT:** To submit the subscription-management deep link URL for your eligible Advanced Commerce API app, use the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

Create the deep link by following these guidelines:

- Follow universal link guidelines for the URL. For more information, see [doc://com.apple.documentation/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content](doc://com.apple.documentation/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).
- Ensure the deep link lands on a page in your app that provides information about the subscription’s state and options for the customer to manage their subscription, for example, to change the plan, or resubscribe.
- Optionally, provide a unique subscription-management deep link URL for each storefront.

## See Also

- [setting-up-your-project-for-advanced-commerce](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/setting-up-your-project-for-advanced-commerce.md)
- [changelog](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/changelog.md)

---


## simulaterefunddeclineonlyinsandboxerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SimulateRefundDeclineOnlyInSandboxError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## skulengthexceedederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SKULengthExceededError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## storefront

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string storefront
```

### 

Use an ISO 3166-1 Alpha-3 country code to represent the storefront.

To get storefront information in your app, use [doc://com.apple.documentation/documentation/StoreKit/Storefront](doc://com.apple.documentation/documentation/StoreKit/Storefront). Get the [doc://com.apple.documentation/documentation/StoreKit/Storefront/countryCode](doc://com.apple.documentation/documentation/StoreKit/Storefront/countryCode) value of the [doc://com.apple.documentation/documentation/StoreKit/Storefront/current](doc://com.apple.documentation/documentation/StoreKit/Storefront/current) storefront, and use that value for `storefront`. Use [doc://com.apple.documentation/documentation/StoreKit/Storefront/updates](doc://com.apple.documentation/documentation/StoreKit/Storefront/updates) to listen for changes to the storefront.

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## storefrontchangeerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object StorefrontChangeError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## subscriptionalreadyexistserror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionAlreadyExistsError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## subscriptioncancelrequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionCancelRequest
```

## See Also

- [Cancel-a-Subscription](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Cancel-a-Subscription.md)
- [SubscriptionCancelResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCancelResponse.md)

---


## subscriptioncancelresponse

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionCancelResponse
```

## 

This is the response body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Cancel-a-Subscription) endpoint.

## See Also

- [Cancel-a-Subscription](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Cancel-a-Subscription.md)
- [SubscriptionCancelRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCancelRequest.md)

---


## subscriptionchangemetadatadescriptors

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionChangeMetadataDescriptors
```

## See Also

- [Change-Subscription-Metadata](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Metadata.md)
- [SubscriptionChangeMetadataRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataRequest.md)
- [SubscriptionChangeMetadataResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataResponse.md)
- [SubscriptionChangeMetadataItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataItem.md)

---


## subscriptionchangemetadataresponse

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionChangeMetadataResponse
```

## 

This is the response body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Metadata) endpoint.

## See Also

- [Change-Subscription-Metadata](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Metadata.md)
- [SubscriptionChangeMetadataRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataRequest.md)
- [SubscriptionChangeMetadataDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataDescriptors.md)
- [SubscriptionChangeMetadataItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionChangeMetadataItem.md)

---


## subscriptioncreateitem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionCreateItem
```

## See Also

- [SubscriptionCreateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionCreateRequest.md)

---


## subscriptiondoesnotexisterror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionDoesNotExistError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## subscriptionmigrateitem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionMigrateItem
```

## See Also

- [Migrate-Subscription-to-Advanced-Commerce-API](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API.md)
- [SubscriptionMigrateRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRequest.md)
- [SubscriptionMigrateResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateResponse.md)
- [SubscriptionMigrateRenewalItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRenewalItem.md)
- [SubscriptionMigrateDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateDescriptors.md)

---


## subscriptionmigraterequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionMigrateRequest
```

## See Also

- [Migrate-Subscription-to-Advanced-Commerce-API](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API.md)
- [SubscriptionMigrateResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateResponse.md)
- [SubscriptionMigrateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateItem.md)
- [SubscriptionMigrateRenewalItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateRenewalItem.md)
- [SubscriptionMigrateDescriptors](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionMigrateDescriptors.md)

---


## subscriptionmodifychangeitem

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionModifyChangeItem
```

## See Also

- [SubscriptionModifyInAppRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyInAppRequest.md)
- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)

---


## subscriptionmodifyinapprequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionModifyInAppRequest
```

## 

You use the `SubscriptionModifyInAppRequest` in your app when the customer makes one or more changes to a subscription, such as upgrading, downgrading, or adding or removing items.

### 

In the following request:

- The customer upgrades the subscription from a monthly to an annual subscription, effective immediately.
- The billing cycle resets.
- The example doesn’t include optional fields in `requestInfo`.

### 

In the following request:

- The customer adds an item to the subscription, effective immediately.
- The billing cycle remains the same. The customer needs to pay the prorated price of the new item. Apple calculates the prorated price and presents a payment sheet to the customer.
- The customer is charged USD 4.99, as indicated by the `price` and `currency` fields in the request, at the next regular billing period.
- The example doesn’t include optional fields in `requestInfo`.

### 

In the following request:

- The customer removes an item from the subscription, effective at the next renewal.
- The billing cycle remains the same.
- The remaining items renew at the next billing period.
- The example doesn’t include optional fields in `requestInfo`.

### 

In the following request:

- The customer downgrades the subscription, effective at the next renewal.
- The billing cycle remains the same.
- The example doesn’t include optional fields in `requestInfo`.

## See Also

- [SubscriptionModifyAddItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyAddItem.md)
- [SubscriptionModifyChangeItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyChangeItem.md)
- [SubscriptionModifyRemoveItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyRemoveItem.md)
- [SubscriptionModifyPeriodChange](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionModifyPeriodChange.md)

---


## subscriptionpricechangerequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionPriceChangeRequest
```

### 

This is the request body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint.

The items array contains [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionPriceChangeItem](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/SubscriptionPriceChangeItem). Include one entry for each SKU within the subscription that has a price change.

## See Also

- [Change-Subscription-Price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Price.md)
- [SubscriptionPriceChangeResponse](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeResponse.md)

---


## subscriptionpricechangeresponse

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionPriceChangeResponse
```

## 

This is the response body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Change-Subscription-Price) endpoint.

## See Also

- [Change-Subscription-Price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Change-Subscription-Price.md)
- [SubscriptionPriceChangeRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionPriceChangeRequest.md)

---


## subscriptionreactivateinapprequest

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionReactivateInAppRequest
```

## See Also

- [SubscriptionReactivateItem](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionReactivateItem.md)

---


## subscriptionrevokeresponse

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object SubscriptionRevokeResponse
```

## 

This is the response body for the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Revoke-Subscription) endpoint.

## See Also

- [Revoke-Subscription](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/Revoke-Subscription.md)
- [SubscriptionRevokeRequest](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SubscriptionRevokeRequest.md)

---


## targetproductid

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string targetProductId
```

## 

You provide the `targetProductId` when you migrate a product using the [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/Migrate-Subscription-to-Advanced-Commerce-API) endpoint.

For more information about generic product IDs, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/creating-your-purchases).

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)

---


## taxCode

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string taxCode
```

## 

You select a tax code for every SKU. For more information, see [doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/taxcodes](doc://com.apple.advancedcommerceapi/documentation/AdvancedCommerceAPI/taxcodes).

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [targetProductId](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/targetProductId.md)

---


## taxcodes

## 

Each SKU, which represents a unique product that your app offers as an in-app purchase, needs a tax code. You provide the tax code value each time you use the Advanced Commerce API to transact.

Use the following table to look up tax codes for your products.

> **NOTE:** Other tax codes are available, similar to those listed in [https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category](https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category). If you don’t see an appropriate tax code for your product in the table below, send a request using the Advanced Commerce API Access form on the [https://developer.apple.com/in-app-purchase/advanced-commerce-api/](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

### 

Select the tax code for your subscription or one-time purchase based on the following tax categories, subcategories, and attributes. You can use the App Store Software category as a default.

| Tax category / Tax subcategory | Selected attributes | Tax code for subscriptions | Tax code for one-time purchases |
| --- | --- | --- | --- |
| App Store Software (Default) | No selectable attributes | C003-00-1 | C003-00-2 |
| Audiobooks / Has ISBN, ISSN, or ECN | Available for offline listening | S007-01-1 | S007-01-2 |
| Audiobooks / Has ISBN, ISSN, or ECN | Available for offline listening  The standard (list) price is displayed  Contains stories with distributed speaker roles, noises, and music | S007-010409-1 | S007-010409-2 |
| Audiobooks / Does not have ISBN, ISSN, or ECN | Available for offline listening | S008-02-1 | S008-02-2 |
| Books / Has ISBN, ISSN, or ECN | Available for offline viewing  The standard (list) price is displayed  Contains interactive features (excluding dictionary, notation, and commenting features)  Contains profane or swear words | S001-03050614-1 | S001-03050614-2 |
| Books / Has ISBN, ISSN, or ECN | Available for offline viewing  The standard (list) price is displayed  Contains profane or swear words  Depicts illegal acts, including theft, assault, drug taking, or robbery | S001-03060714-1 | S001-03060714-2 |
| Books / Does not have ISBN, ISSN, or ECN | Available for offline viewing  A complete book (not an excerpt)  Contains profane or swear words  Depicts illegal acts, including theft, assault, drug taking, or robbery | S002-02040708-1 | S002-02040708-2 |
| Boosting | No selectable attributes | N/A | C025-00-2 |
| Games | Primarily played online | C009-0102-1 | C009-01-2 |
| Video / Pay-Per-View | No attribute selected | N/A | S022-00-2 |
| Video / Pay-Per-View | Exclusively features live TV broadcasting and/or linear programming | N/A | S022-01-2 |
| Video / Purchase for permanent access | Content is available for offline viewing | N/A | S020-01-2 |
| Video / Rental | Content is primarily accessed through streaming | N/A | S019-01-2 |
| Video / Subscription | No attribute selected | S021-08-1 | S021-08-2 |
| Video / Subscription | Live TV broadcasting and/or linear programming make up more than 10% of total content | S021-0308-1 | S021-0308-2 |

For more information about tax categories, see [https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category](https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category).

## See Also

- [prices](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/prices.md)
- [handling-subscription-price-changes](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/handling-subscription-price-changes.md)

---


## transactionId

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string transactionId
```

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)

---


## transactionidnotfounderror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object TransactionIdNotFoundError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## transactionnotrefundableerror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object TransactionNotRefundableError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## unauthorizederror

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
object UnauthorizedError
```

## See Also

- [ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError.md)
- [AlreadyRefundedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AlreadyRefundedError.md)
- [AtLeastOneItemError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneItemError.md)
- [AtLeastOneOfDisplayNameOrDescriptionError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/AtLeastOneOfDisplayNameOrDescriptionError.md)
- [BillingCycleResetWithEffectiveLaterError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/BillingCycleResetWithEffectiveLaterError.md)
- [ChangeItemNotFoundError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/ChangeItemNotFoundError.md)
- [CurrentSKULengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/CurrentSKULengthExceededError.md)
- [DependentSKUsCannotBeChainedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeChainedError.md)
- [DependentSKUsCannotBeSharedError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DependentSKUsCannotBeSharedError.md)
- [DescriptionLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DescriptionLengthExceededError.md)
- [DisplayNameLengthExceededError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/DisplayNameLengthExceededError.md)
- [EmptyAddChangeItemsError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/EmptyAddChangeItemsError.md)
- [GeneralInternalError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalError.md)
- [GeneralInternalRetryableError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/GeneralInternalRetryableError.md)
- [InactiveACASubError](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/InactiveACASubError.md)

---


## version

## Declaration

**Platforms:** Unsupported OS: Advanced Commerce API

```swift
string version
```

## See Also

- [currency](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/currency.md)
- [description](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/description.md)
- [dependentSKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/dependentSKU.md)
- [displayName](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/displayName.md)
- [effective](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/effective.md)
- [period](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/period.md)
- [price](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/price.md)
- [proratedPrice](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/proratedPrice.md)
- [retainBillingCycle](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/retainBillingCycle.md)
- [refundAmount](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundAmount.md)
- [refundReason](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundReason.md)
- [refundRiskingPreference](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/refundRiskingPreference.md)
- [SKU](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/SKU.md)
- [storefront](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/storefront.md)
- [taxCode](../com.apple.advancedcommerceapi/AdvancedCommerceAPI/taxCode.md)

---

