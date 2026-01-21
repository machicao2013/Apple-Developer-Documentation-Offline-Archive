# appstorereceipts

*Merged documentation for appstorereceipts*

---

# App Store Receipts

## 

> **IMPORTANT:** The [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt) endpoint is deprecated. To validate receipts on your server, follow the steps in [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/validating-receipts-on-the-device](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/validating-receipts-on-the-device) on your server.

Your server can access the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt) endpoint to validate app and in-app transaction receipts. Submit a receipt to the App Store with your [https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts) to receive a JSON response containing the app information and in-app purchase details in the fields that make up the receipt. Each field or combination of fields provides insight you can use to deliver service and content to the user, as you define.

In-app transactions that your app doesn’t mark as finished using [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)) or [doc://com.apple.documentation/documentation/StoreKit/Transaction/finish()](doc://com.apple.documentation/documentation/StoreKit/Transaction/finish()) remain in the App Store receipt. Auto-renewable subscriptions, non-renewing subscriptions, and non-consumables remain in the receipt indefinitely, and appear in the customer transaction history when you call the [doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Transaction-History-V1](doc://com.apple.documentation/documentation/AppStoreServerAPI/Get-Transaction-History-V1) endpoint.

The [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) object for auto-renewable subscriptions can grow over time because the renewal transactions stay in the receipt indefinitely. To optimize performance, the App Store may truncate receipts in the sandbox environment to remove old transactions.

You can test validating receipts in the sandbox environment. For more information, see [doc://com.apple.documentation/documentation/StoreKit/testing-in-app-purchases-with-sandbox](doc://com.apple.documentation/documentation/StoreKit/testing-in-app-purchases-with-sandbox) and [https://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases](https://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases).

You can validate receipts from the App Store using server-side receipt validation or on-device validation. For more information about receipt validation options, see [doc://com.apple.documentation/documentation/StoreKit/choosing-a-receipt-validation-technique](doc://com.apple.documentation/documentation/StoreKit/choosing-a-receipt-validation-technique).

> **NOTE:** Session 110404: [https://developer.apple.com/videos/play/wwdc2022/110404/](https://developer.apple.com/videos/play/wwdc2022/110404/).

## Topics

### Receipt data

- [app-store-receipt-data-types](../com.apple.appstorereceipts/AppStoreReceipts/app-store-receipt-data-types.md)

### Local receipt validation

- [validating-receipts-on-the-device](../com.apple.appstorereceipts/AppStoreReceipts/validating-receipts-on-the-device.md)

### Deprecated

- [Verify-Receipt](../com.apple.appstorereceipts/AppStoreReceipts/Verify-Receipt.md)
- [requestBody](../com.apple.appstorereceipts/AppStoreReceipts/requestBody.md)
- [responseBody](../com.apple.appstorereceipts/AppStoreReceipts/responseBody.md)
- [error](../com.apple.appstorereceipts/AppStoreReceipts/error.md)

---


# Detailed Documentation


## responseBody


### Receipt-data.dictionary


#### In_app-data.dictionary

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object responseBody.Receipt.In_app
```

## 

The `in_app` array is not in chronological order. When parsing the array, iterate over all items to ensure all items are fulfilled. For example, you cannot assume that the last item in the array is the most recent.

For receipts containing auto-renewable subscriptions, check the value of the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) key of the response to get the status of the most recent renewal.

You can use this array to:

- Check for an empty array in a valid receipt, indicating that the App Store has made no in-app purchase charges.
- Determine which products the user purchased. Purchases for non-consumable products, auto-renewable subscriptions, and non-renewing subscriptions remain in the receipt indefinitely. For consumable products, the transaction is added to the receipt when the purchase is made, and remains until your app finishes that transaction. It no longer appears in updated receipts after you call [doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)](doc://com.apple.documentation/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)).

---


### Latest_receipt_info-data.dictionary

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object responseBody.Latest_receipt_info
```

## See Also

- [Pending_renewal_info-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary.md)
- [Receipt-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Receipt-data.dictionary.md)

---


### Pending_renewal_info-data.dictionary

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object responseBody.Pending_renewal_info
```

## 

In the JSON file, `pending_renewal_info` is an array in which each element contains the pending renewal information for each auto-renewable subscription identified by the `product_id`. A pending renewal may refer to a renewal that the system scheduled in the future or a renewal that failed in the past for some reason.

Use this value to get critical information about any pending renewal transactions for an auto-renewable subscription.

The `pending_renewal_info` array is returned only for app receipts that contain auto-renewable subscriptions. If customers voluntarily cancel a subscription renewal while in the grace period, the App Store pauses billing retry, and removes the transaction from `pending_renewal_info`. The subscription is in the grace period if the key `grace_period_expires_date_ms` is present and the expiration date hasn’t passed.

## See Also

- [Latest_receipt_info-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary.md)
- [Receipt-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Receipt-data.dictionary.md)

---


### Receipt-data.dictionary

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object responseBody.Receipt
```

## Topics

### Objects

- [In_app-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary.md)

## See Also

- [Pending_renewal_info-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary.md)
- [Latest_receipt_info-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary.md)

---


## Verify-Receipt

## 

Validating with the App Store requires a secure connection between your app and your server, as well as code on your server to validate the receipt with the App Store. Submit an HTTP POST request with the contents detailed in [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/requestBody](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/requestBody) using the `verifyReceipt` endpoint to verify receipts with the App Store. Use the receipt fields in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody) to validate app and in-app purchases.

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to call this endpoint.

For more information about server-side receipt validation, see [doc://com.apple.documentation/documentation/StoreKit/validating-receipts-with-the-app-store](doc://com.apple.documentation/documentation/StoreKit/validating-receipts-with-the-app-store).

### 

The sandbox URL for verifying receipts is:

```other
POST https://sandbox.itunes.apple.com/verifyReceipt
```

> **IMPORTANT:** As a best practice, always call the production URL `https://buy.itunes.apple.com/verifyReceipt` first and proceed to verify with the sandbox URL if you receive a `21007` [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/status](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/status) code. Following this approach ensures that you don’t have to switch between URLs while your app is in testing, in review by App Review, or live in the App Store.

### 

The `verifyReceipt` endpoint is deprecated. The HTTP header includes the deprecation date, according to [https://www.rfc-editor.org/rfc/rfc8594.html](https://www.rfc-editor.org/rfc/rfc8594.html).

## See Also

- [requestBody](../com.apple.appstorereceipts/AppStoreReceipts/requestBody.md)
- [responseBody](../com.apple.appstorereceipts/AppStoreReceipts/responseBody.md)
- [error](../com.apple.appstorereceipts/AppStoreReceipts/error.md)

---


## app-store-receipt-data-types

## Topics

### Transaction identifiers

- [original_transaction_id](../com.apple.appstorereceipts/AppStoreReceipts/original_transaction_id.md)
- [transaction_id](../com.apple.appstorereceipts/AppStoreReceipts/transaction_id.md)
- [app_account_token](../com.apple.appstorereceipts/AppStoreReceipts/app_account_token.md)

### Receipt and subscription status

- [status](../com.apple.appstorereceipts/AppStoreReceipts/status.md)
- [auto_renew_status](../com.apple.appstorereceipts/AppStoreReceipts/auto_renew_status.md)
- [is_in_billing_retry_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_billing_retry_period.md)
- [is_in_intro_offer_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_intro_offer_period.md)
- [is_trial_period](../com.apple.appstorereceipts/AppStoreReceipts/is_trial_period.md)

### Dates and intent

- [expiration_intent](../com.apple.appstorereceipts/AppStoreReceipts/expiration_intent.md)
- [cancellation_date_ms](../com.apple.appstorereceipts/AppStoreReceipts/cancellation_date_ms.md)
- [expires_date_ms](../com.apple.appstorereceipts/AppStoreReceipts/expires_date_ms.md)

### Promotions and offers

- [promotional_offer_id](../com.apple.appstorereceipts/AppStoreReceipts/promotional_offer_id.md)
- [offer_code_ref_name](../com.apple.appstorereceipts/AppStoreReceipts/offer_code_ref_name.md)

### Family Sharing

- [in_app_ownership_type](../com.apple.appstorereceipts/AppStoreReceipts/in_app_ownership_type.md)

---


## app_account_token

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string app_account_token
```

## 

When a customer initiates an in-app purchase, you can optionally generate an [doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)](doc://com.apple.documentation/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) and send it to the App Store. The App Store returns the same value in [doc://com.apple.documentation/documentation/StoreKit/Transaction/appAccountToken](doc://com.apple.documentation/documentation/StoreKit/Transaction/appAccountToken) in the transaction information after the customer completes the purchase.

If you’re using the [doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase) and provide a UUID in the [doc://com.apple.documentation/documentation/StoreKit/SKMutablePayment/applicationUsername](doc://com.apple.documentation/documentation/StoreKit/SKMutablePayment/applicationUsername) property, then the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/app_account_token](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/app_account_token) field contains that value.

## See Also

- [original_transaction_id](../com.apple.appstorereceipts/AppStoreReceipts/original_transaction_id.md)
- [transaction_id](../com.apple.appstorereceipts/AppStoreReceipts/transaction_id.md)

---


## auto_renew_status

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string auto_renew_status
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary) array.

The value for this field should not be interpreted as the customer’s subscription status. You can use this value to display an alternative subscription product in your app, such as a lower-level subscription plan to which the user can downgrade from their current plan.

Consider presenting an attractive upgrade or downgrade offer in the same subscription group, if the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/auto_renew_status](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/auto_renew_status) value is `“0”`. See [https://developer.apple.com/videos/play/wwdc2018/705/](https://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 for more information.

## See Also

- [status](../com.apple.appstorereceipts/AppStoreReceipts/status.md)
- [is_in_billing_retry_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_billing_retry_period.md)
- [is_in_intro_offer_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_intro_offer_period.md)
- [is_trial_period](../com.apple.appstorereceipts/AppStoreReceipts/is_trial_period.md)

---


## cancellation_date_ms

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string cancellation_date_ms
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

This field represents the time and date the App Store refunded a transaction or revoked it from family sharing, in UNIX epoch time format, in milliseconds. This field is only present for purchases that Apple refunded or revoked. Use this time format for processing dates.

A canceled in-app purchase remains in the receipt indefinitely. This value is present only if the refund or revocation was for a non-consumable product, an auto-renewable subscription, or a non-renewing subscription.

Use this value to determine whether to stop providing the content associated with the purchase.

## See Also

- [expiration_intent](../com.apple.appstorereceipts/AppStoreReceipts/expiration_intent.md)
- [expires_date_ms](../com.apple.appstorereceipts/AppStoreReceipts/expires_date_ms.md)

---


## error

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object error
```

## See Also

- [Verify-Receipt](../com.apple.appstorereceipts/AppStoreReceipts/Verify-Receipt.md)
- [requestBody](../com.apple.appstorereceipts/AppStoreReceipts/requestBody.md)
- [responseBody](../com.apple.appstorereceipts/AppStoreReceipts/responseBody.md)

---


## expiration_intent

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string expiration_intent
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary) array.

You can use this value to do the following:

- If the value is `"1"`, decide whether to survey the subscribers who have opted in to an account on your system or show alternative subscription products within the same group. Decide whether to present a subscription offer to win back the user.
- If the value is `"2"`, decide whether to show the same or alternative subscription products because the user didn’t actively make the choice to unsubscribe.

For more information, see [https://developer.apple.com/videos/play/wwdc2018/705/](https://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 and [doc://com.apple.documentation/documentation/StoreKit/implementing-promotional-offers-in-your-app](doc://com.apple.documentation/documentation/StoreKit/implementing-promotional-offers-in-your-app).

## See Also

- [cancellation_date_ms](../com.apple.appstorereceipts/AppStoreReceipts/cancellation_date_ms.md)
- [expires_date_ms](../com.apple.appstorereceipts/AppStoreReceipts/expires_date_ms.md)

---


## expires_date_ms

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string expires_date_ms
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

The time a subscription expires or when it will renew, in UNIX epoch time format, in milliseconds. Use this time format for processing dates.

You can use this date value to:

- Manage auto-renewable subscriptions. Store this value, `original_transaction_id`, `product_id`, and `purchase_date_ms` for each subscription, as a best practice.
- Identify the date the subscription renews or expires.
- Determine a user’s access to content or a service by comparing this date to the current date. After validating the latest receipt, continue providing service if the date is in the future. If the subscription expiration date for the latest renewal transaction has passed, the subscription has expired.

## See Also

- [expiration_intent](../com.apple.appstorereceipts/AppStoreReceipts/expiration_intent.md)
- [cancellation_date_ms](../com.apple.appstorereceipts/AppStoreReceipts/cancellation_date_ms.md)

---


## in_app_ownership_type

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string in_app_ownership_type
```

## 

When family members benefit from a shared subscription, App Store updates their receipt to include the family-shared purchase. Use the value of [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/in_app_ownership_type](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/in_app_ownership_type) to understand whether a transaction belongs to the purchaser or a family member who benefits.

This field appears in the App Store server notifications unified receipt ([doc://com.apple.documentation/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary](doc://com.apple.documentation/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary)) and in transaction receipts ([doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary)).

For more information about Family Sharing, see [doc://com.apple.documentation/documentation/StoreKit/supporting-family-sharing-in-your-app](doc://com.apple.documentation/documentation/StoreKit/supporting-family-sharing-in-your-app).

---


## is_in_billing_retry_period

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string is_in_billing_retry_period
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary) array.

This field indicates whether Apple is attempting to renew an expired subscription automatically. If the customer’s subscription failed to renew because the App Store was unable to complete the transaction, this value reflects whether the App Store is still trying to renew the subscription.

The subscription retry flag is solely indicative of whether a subscription is in a billing retry state. Use this value in conjunction with `expiration_intent`, `expires_date`, and `transaction_id` for more insight.

You can use this field to:

- Determine that the user has been billed successfully, if this field has been removed and there is a new transaction with a future `expires_date`.
- Inform the user that there may be an issue with their billing information, if the value is `“1”`. For example, an expired credit card or insufficient balance could prevent this customer’s account from being billed.
- Implement a grace period to improve recovery, if the value is `“1”` and the `expires_date` is in the past. A grace period is free or limited subscription access while a subscriber is in a billing retry state. See [https://developer.apple.com/videos/play/wwdc2018/705/](https://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 for more information.

## See Also

- [status](../com.apple.appstorereceipts/AppStoreReceipts/status.md)
- [auto_renew_status](../com.apple.appstorereceipts/AppStoreReceipts/auto_renew_status.md)
- [is_in_intro_offer_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_intro_offer_period.md)
- [is_trial_period](../com.apple.appstorereceipts/AppStoreReceipts/is_trial_period.md)

---


## is_in_intro_offer_period

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string is_in_intro_offer_period
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

You can use this value to determine if the user is eligible for introductory pricing. If a previous subscription period in the receipt has the value `“true”` for either the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/is_trial_period](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/is_trial_period) or `is_in_intro_offer_period` keys, the user is not eligible for a free trial or introductory price within that subscription group. For more information, see [doc://com.apple.documentation/documentation/StoreKit/implementing-introductory-offers-in-your-app](doc://com.apple.documentation/documentation/StoreKit/implementing-introductory-offers-in-your-app).

## See Also

- [status](../com.apple.appstorereceipts/AppStoreReceipts/status.md)
- [auto_renew_status](../com.apple.appstorereceipts/AppStoreReceipts/auto_renew_status.md)
- [is_in_billing_retry_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_billing_retry_period.md)
- [is_trial_period](../com.apple.appstorereceipts/AppStoreReceipts/is_trial_period.md)

---


## is_trial_period

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string is_trial_period
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

You can use this value to determine whether the specific record is in a subscription trial period. If a previous subscription period in the receipt has the value `"true"` for either the `is_trial_period` or [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/is_in_intro_offer_period](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/is_in_intro_offer_period) keys, the user is not eligible for a free trial or introductory price within that subscription group.

## See Also

- [status](../com.apple.appstorereceipts/AppStoreReceipts/status.md)
- [auto_renew_status](../com.apple.appstorereceipts/AppStoreReceipts/auto_renew_status.md)
- [is_in_billing_retry_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_billing_retry_period.md)
- [is_in_intro_offer_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_intro_offer_period.md)

---


## offer_code_ref_name

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string offer_code_ref_name
```

## 

When a customer successfully redeems an offer code, this field is present in the receipt and contains the reference name of the offer. You establish the offer reference name in App Store Connect when you configure offers and create the offer codes. For more information about setting up offers, see [https://help.apple.com/app-store-connect/#/dev6a098e4b1](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

Use this value to:

- Determine whether the sale of the subscription was from an offer code campaign.
- Determine the specific offer the customer redeemed.
- Keep track of subscription-offer codes a customer has redeemed, to limit discounts you offer, according to your business model.

For more information on offers and offer codes, see [doc://com.apple.documentation/documentation/StoreKit/implementing-offer-codes-in-your-app](doc://com.apple.documentation/documentation/StoreKit/implementing-offer-codes-in-your-app).

## See Also

- [promotional_offer_id](../com.apple.appstorereceipts/AppStoreReceipts/promotional_offer_id.md)

---


## original_transaction_id

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string original_transaction_id
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary), [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary), and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

This value is identical to the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/transaction_id](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/transaction_id) except when the user restores a purchase or renews a subscription. This value has the same format as the transaction’s `transactionIdentifier` property; however, the values may not be the same. For auto-renewable subscription transactions, this value also appears in the `pending_renewal_info` key of the JSON response.

You can use this value to:

- Match a transaction found in the receipt to a server-to-server notification event. For more information, see [doc://com.apple.documentation/documentation/StoreKit/enabling-app-store-server-notifications](doc://com.apple.documentation/documentation/StoreKit/enabling-app-store-server-notifications).
- Manage auto-renewable subscriptions. Store this value, `product_id`, `expires_date_ms`, and `purchase_date_ms` for each transaction for each customer, as a best practice.
- Identify a subscription with the `product_id` in the `pending_renewal_info` section. Do not rely on the `original_transaction_id` value on its own. Treat this purchase as a new subscription when you see a new `original_transaction_id` value for a `product_id`.
- Differentiate a purchase transaction from a restore or a renewal transaction. In a purchase transaction, the `transaction_id` always matches the `original_transaction_id`. For subscriptions, it indicates the first subscription purchase. For a restore or renewal, the `transaction_id` does not match the `original_transaction_id`.
- Identify one or more renewals for the same subscription.

## See Also

- [transaction_id](../com.apple.appstorereceipts/AppStoreReceipts/transaction_id.md)
- [app_account_token](../com.apple.appstorereceipts/AppStoreReceipts/app_account_token.md)

---


## promotional_offer_id

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string promotional_offer_id
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

You provide this value in the Promotional Offer Identifier field when you create the promotional offer in App Store Connect. For more information, see [https://help.apple.com/app-store-connect/#/dev16dfca448](https://help.apple.com/app-store-connect/#/dev16dfca448).

You can use the promotional offer ID value to:

- Confirm that the sale of the subscription was from a promotional offer.
- Confirm which promotional offer the user redeemed.
- Keep track of the promotional offers that a user has redeemed to limit discounts you offer, according to your business model.

For more information on promotional offers, see [doc://com.apple.documentation/documentation/StoreKit/implementing-promotional-offers-in-your-app](doc://com.apple.documentation/documentation/StoreKit/implementing-promotional-offers-in-your-app).

## See Also

- [offer_code_ref_name](../com.apple.appstorereceipts/AppStoreReceipts/offer_code_ref_name.md)

---


## requestBody

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object requestBody
```

## 

To receive a decoded receipt for validation, send a request with the encoded receipt data and app password to the App Store. For receipts that contain auto-renewable subscriptions, optionally include an exclusion flag. Send this JSON data using the HTTP POST request method.

## See Also

- [Verify-Receipt](../com.apple.appstorereceipts/AppStoreReceipts/Verify-Receipt.md)
- [responseBody](../com.apple.appstorereceipts/AppStoreReceipts/responseBody.md)
- [error](../com.apple.appstorereceipts/AppStoreReceipts/error.md)

---


## responseBody

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
object responseBody
```

## 

The [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt) endpoint returns this response.

## Topics

### Objects

- [Pending_renewal_info-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary.md)
- [Latest_receipt_info-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary.md)
- [Receipt-data.dictionary](../com.apple.appstorereceipts/AppStoreReceipts/responseBody/Receipt-data.dictionary.md)

## See Also

- [Verify-Receipt](../com.apple.appstorereceipts/AppStoreReceipts/Verify-Receipt.md)
- [requestBody](../com.apple.appstorereceipts/AppStoreReceipts/requestBody.md)
- [error](../com.apple.appstorereceipts/AppStoreReceipts/error.md)

---


## status

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
int status
```

## 

The [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/Verify-Receipt) endpoint returns this field in the JSON response, [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody).

The value for `status` is `0` if the receipt is valid, or a status code if there’s an error. The status code reflects the status of the app receipt as a whole. For example, if you send a valid app receipt that contains an expired subscription, the response is `0` because the receipt is valid.

Status codes `21100–21199` are various internal data access errors.

## See Also

- [auto_renew_status](../com.apple.appstorereceipts/AppStoreReceipts/auto_renew_status.md)
- [is_in_billing_retry_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_billing_retry_period.md)
- [is_in_intro_offer_period](../com.apple.appstorereceipts/AppStoreReceipts/is_in_intro_offer_period.md)
- [is_trial_period](../com.apple.appstorereceipts/AppStoreReceipts/is_trial_period.md)

---


## transaction_id

## Declaration

**Platforms:** Unsupported OS: App Store Receipts

```swift
string transaction_id
```

## 

This field is returned in the JSON response, in the [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) and [doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary](doc://com.apple.appstorereceipts/documentation/AppStoreReceipts/responseBody/Receipt-data.dictionary/In_app-data.dictionary) arrays.

This value has the same format as the transaction’s [doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier](doc://com.apple.documentation/documentation/StoreKit/SKPaymentTransaction/transactionIdentifier) property; however, the values may not be the same.

You can use this value to:

- Manage subscribers in your account database. Store the `transaction_id`, `original_transaction_id`, and `product_id` for each transaction, as a best practice to store transaction records for each customer. App Store generates a new value for `transaction_id` every time the subscription automatically renews or is restored on a new device.
- Differentiate a purchase transaction from a restore or a renewal transaction. In a purchase transaction, the `transaction_id` always matches the `original_transaction_id`. For subscriptions, it indicates the first subscription purchase. For a restore or renewal, the `transaction_id` does not match the `original_transaction_id`. If a user restores or renews the same purchase multiple times, each restore or renewal has a different `transaction_id`.

## See Also

- [original_transaction_id](../com.apple.appstorereceipts/AppStoreReceipts/original_transaction_id.md)
- [app_account_token](../com.apple.appstorereceipts/AppStoreReceipts/app_account_token.md)

---


## validating-receipts-on-the-device

## 

When users install apps from the App Store, the app contains a cryptographically signed receipt that Apple creates and stores inside the app bundle, which you can then validate.

> **NOTE:** The receipt isn’t necessary if you use [doc://com.apple.documentation/documentation/StoreKit/AppTransaction](doc://com.apple.documentation/documentation/StoreKit/AppTransaction) to validate the app download, or [doc://com.apple.documentation/documentation/StoreKit/Transaction](doc://com.apple.documentation/documentation/StoreKit/Transaction) to validate in-app purchases. Only use the receipt if your app uses the [doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase](doc://com.apple.documentation/documentation/StoreKit/original-api-for-in-app-purchase), or needs the receipt to validate the app download because it can’t use [doc://com.apple.documentation/documentation/StoreKit/AppTransaction](doc://com.apple.documentation/documentation/StoreKit/AppTransaction).

Validating the receipt locally requires you to develop or use code to read and decode the receipt as a PKCS #7 container, as defined by [https://www.rfc-editor.org/rfc/rfc2315](https://www.rfc-editor.org/rfc/rfc2315). The App Store encodes the payload of the container using Abstract Syntax Notation One (ASN.1), as defined by [https://www.itu.int/rec/T-REC-X.690/](https://www.itu.int/rec/T-REC-X.690/). The payload contains a set of receipt attributes. Each receipt attribute contains a type, a version, and a value.

The App Store defines the structure of the payload with the following ASN.1 notation:

```other
ReceiptModule DEFINITIONS ::=
BEGIN

ReceiptAttribute ::= SEQUENCE {
    type    INTEGER,
    version INTEGER,
    value   OCTET STRING
}

Payload ::= SET OF ReceiptAttribute

END
```

### 

In macOS and Mac apps built with Mac Catalyst, implement receipt validation in the main function, before the app calls [doc://com.apple.documentation/documentation/AppKit/NSApplicationMain(_:_:)](doc://com.apple.documentation/documentation/AppKit/NSApplicationMain(_:_:)).

To validate the app receipt, perform the following tests in order:

1. Locate and load the app receipt from the app’s bundle. The class [doc://com.apple.documentation/documentation/Foundation/Bundle](doc://com.apple.documentation/documentation/Foundation/Bundle) provides the location of the receipt with the property [doc://com.apple.documentation/documentation/Foundation/Bundle/appStoreReceiptURL](doc://com.apple.documentation/documentation/Foundation/Bundle/appStoreReceiptURL).
2. Decode the app receipt as a PKCS #7 container and verify that the chain of trust for the container’s signature traces back to the Apple Inc. Root certificate, available from [https://www.apple.com/certificateauthority/](https://www.apple.com/certificateauthority/). Use the `receipt_creation_date`, identified as [https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1) when validating the receipt signature.
3. Verify that the bundle identifier, identified as [https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1), matches your app’s bundle identifier.
4. Verify that the version identifier string, identified as [https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1), matches the version string in your app’s bundle.
5. Compute a SHA-1 hash for the device that installs the app and verify that it matches the receipt’s hash, identified as [https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1).

The validation passes if all of the tests pass. If any test fails, the validation fails.

For information about the keys in a receipt, see [https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1).

### 

Decode the app receipt as a PKCS #7 container and verify that the chain of trust for the container’s signature traces back to the Apple Inc. Root certificate, available from [https://www.apple.com/certificateauthority/](https://www.apple.com/certificateauthority/).

> **TIP:** Don’t hardcode intermediate certificates in your app. Ensure that your code supports certificates that use SHA-256 and SHA-1 signing algorithms.

Make sure your app uses the date from the `receipt_creation_date` field, identified as [https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW1), to validate the receipt’s signature. Many cryptographic libraries default to using the device’s current time and date when validating a PKCS #7 package, but this may not produce the correct results when validating a receipt’s signature. For example, if the receipt was signed with a valid certificate, but the certificate has since expired, using the device’s current date incorrectly returns an invalid result.

### 

Compute the SHA-1 hash to match the local device with the device hash inside the App Store reciept. When computing the SHA-1 hash, use the platform-specific data source. The source of bytes for each platform is:

- watchOS: Use the raw bytes from the [doc://com.apple.documentation/documentation/Foundation/UUID/uuid](doc://com.apple.documentation/documentation/Foundation/UUID/uuid) property of the [doc://com.apple.documentation/documentation/Foundation/UUID](doc://com.apple.documentation/documentation/Foundation/UUID) that [doc://com.apple.documentation/documentation/WatchKit/WKInterfaceDevice/identifierForVendor](doc://com.apple.documentation/documentation/WatchKit/WKInterfaceDevice/identifierForVendor) provides.
- iOS, iPadOS, tvOS, and iOS apps running on a Mac with Apple silicon: Use the raw bytes from the [doc://com.apple.documentation/documentation/Foundation/UUID/uuid](doc://com.apple.documentation/documentation/Foundation/UUID/uuid) property of the [doc://com.apple.documentation/documentation/Foundation/UUID](doc://com.apple.documentation/documentation/Foundation/UUID) that [doc://com.apple.documentation/documentation/UIKit/UIDevice/identifierForVendor](doc://com.apple.documentation/documentation/UIKit/UIDevice/identifierForVendor) provides.
- macOS and apps built with Mac Catalyst: Use the data that returns from `copy_mac_address` from the example code below.

The following two code examples illustrate how to retrieve an identifier in macOS, as the `copy_mac_address` function shows, for validating an App Store receipt.

In the following Swift code, the `io_service` function uses [doc://com.apple.documentation/documentation/iokit](doc://com.apple.documentation/documentation/iokit) to retrieve network interfaces as an optional [doc://com.apple.documentation/documentation/iokit](doc://com.apple.documentation/documentation/iokit) object. The `copy_mac_address` function looks up an appropriate network interface and returns the hardware address from the [doc://com.apple.documentation/documentation/iokit](doc://com.apple.documentation/documentation/iokit) object as optional `CFData`.

```swift
import IOKit
import Foundation

// Returns an object with a +1 retain count; the caller needs to release.
func io_service(named name: String, wantBuiltIn: Bool) -> io_service_t? {
    let default_port = kIOMasterPortDefault
    var iterator = io_iterator_t()
    defer {
        if iterator != IO_OBJECT_NULL {
            IOObjectRelease(iterator)
        }
    }

    guard let matchingDict = IOBSDNameMatching(default_port, 0, name),
        IOServiceGetMatchingServices(default_port,
                                     matchingDict as CFDictionary,
                                     &iterator) == KERN_SUCCESS,
        iterator != IO_OBJECT_NULL
    else {
        return nil
    }

    var candidate = IOIteratorNext(iterator)
    while candidate != IO_OBJECT_NULL {
        if let cftype = IORegistryEntryCreateCFProperty(candidate,
                                                        "IOBuiltin" as CFString,
                                                        kCFAllocatorDefault,
                                                        0) {
            let isBuiltIn = cftype.takeRetainedValue() as! CFBoolean
            if wantBuiltIn == CFBooleanGetValue(isBuiltIn) {
                return candidate
            }
        }

        IOObjectRelease(candidate)
        candidate = IOIteratorNext(iterator)
    }

    return nil
}

func copy_mac_address() -> CFData? {
    // Prefer built-in network interfaces.
    // For example, an external Ethernet adaptor can displace
    // the built-in Wi-Fi as en0.
    guard let service = io_service(named: "en0", wantBuiltIn: true)
            ?? io_service(named: "en1", wantBuiltIn: true)
            ?? io_service(named: "en0", wantBuiltIn: false)
        else { return nil }
    defer { IOObjectRelease(service) }

    if let cftype = IORegistryEntrySearchCFProperty(
        service,
        kIOServicePlane,
        "IOMACAddress" as CFString,
        kCFAllocatorDefault,
        IOOptionBits(kIORegistryIterateRecursively | kIORegistryIterateParents)) {
            return (cftype as! CFData)
    }

    return nil
}
```

The following Objective-C code works in the same fashion. This example uses [doc://com.apple.documentation/documentation/iokit](doc://com.apple.documentation/documentation/iokit) to look up the relevant network interface, and returns the bytes that identify the built-in network interface:

```objc
#import <Foundation/Foundation.h>
#import <IOKit/network/IONetworkLib.h>

io_service_t io_service(const char *name, BOOL wantBuiltIn) {
    io_iterator_t iterator = IO_OBJECT_NULL;
    mach_port_t default_port = kIOMasterPortDefault;
    io_service_t service = IO_OBJECT_NULL;

    if (KERN_SUCCESS != IOMasterPort(MACH_PORT_NULL, &default_port)) {
        return IO_OBJECT_NULL;
    }

    CFMutableDictionaryRef matchingDict = IOBSDNameMatching(default_port,
                                                            0,
                                                            name);
    if (matchingDict == NULL) {
        return IO_OBJECT_NULL;
    }

    if (KERN_SUCCESS != IOServiceGetMatchingServices(default_port,
                                                     matchingDict,
                                                     &iterator)) {
        return IO_OBJECT_NULL;
    }

    if (iterator != IO_OBJECT_NULL) {
        io_service_t candidate = IOIteratorNext(iterator);
        while (candidate != IO_OBJECT_NULL) {
            CFTypeRef isBuiltIn =
            IORegistryEntryCreateCFProperty(candidate,
                                            CFSTR(kIOBuiltin),
                                            kCFAllocatorDefault,
                                            0);
            if (isBuiltIn != NULL && CFGetTypeID(isBuiltIn) == CFBooleanGetTypeID()) {
                if (wantBuiltIn == CFBooleanGetValue(isBuiltIn)) {
                    service = candidate;
                    break;
                }
            }

            IOObjectRelease(candidate);
            candidate = IOIteratorNext(iterator);
        }
        IOObjectRelease(iterator);
    }

    return service;
}

CFDataRef copy_mac_address() {
    CFDataRef macAddress = NULL;
    io_service_t service = io_service("en0", true);

    if (service == IO_OBJECT_NULL) {
        service = io_service("en1", true);
    }

    if (service == IO_OBJECT_NULL) {
        service = io_service("en0", false);
    }

    if (service != IO_OBJECT_NULL) {
        CFTypeRef property =
        IORegistryEntrySearchCFProperty(service,
                                        kIOServicePlane,
                                        CFSTR(kIOMACAddress),
                                        kCFAllocatorDefault,
                                        kIORegistryIterateRecursively | kIORegistryIterateParents);
        if (property != NULL) {
            if (CFGetTypeID(property) == CFDataGetTypeID()) {
                macAddress = property;
            }
            else {
                CFRelease(property);
            }
        }

        IOObjectRelease(service);
    }

    return macAddress;
}
```

### 

If your app receipt validation fails, respond to that failure as follows:

- Don’t try to terminate the app. Without a validated receipt, assume the user doesn’t have access to premium content. Provide a user interface to gracefully handle this case and inform the user what they can do to get full access to your app’s features.
- If the app receipt is missing or corrupt, use the [doc://com.apple.documentation/documentation/StoreKit/SKReceiptRefreshRequest](doc://com.apple.documentation/documentation/StoreKit/SKReceiptRefreshRequest) object to refresh the app receipt.
- In the sandbox environment, if the app receipt is missing, assume the tester is a new customer and doesn’t have access to premium content.

> **NOTE:** For apps in iOS and iPadOS running in the sandbox environment and in StoreKit testing in Xcode, the app receipt is present only after the tester makes their first in-app purchase. The app receipt is always present in TestFlight on devices running macOS.

---

