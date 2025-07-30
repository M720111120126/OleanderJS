# router Usage Documentation

## Overview
`router` is a simple static class used to manage browser navigation operations. This class provides two methods: `pushUrl` and `back`, used to navigate to a new URL and return to the previous page or replace the current page, respectively.

## Method Description

### 1. Navigate to a New URL
```javascript
router.pushUrl(url);
```
**Function**: Navigates the browser to the specified URL.
**Parameters**:
- `url`: String type, the target URL address.

### 2. Return to Previous Page or Replace Current Page
```javascript
router.back(url);
```
**Function**: If no URL is provided, returns to the previous page in the browser history; if a URL is provided, replaces the current page with the specified URL.
**Parameters**:
- `url`: String type, optional parameter, the target URL address. If not provided, a back operation is performed by default.

## Example Code

The following is a simple example demonstrating how to use `router` for basic navigation operations:

```javascript
// Navigate to a new URL
router.pushUrl("https://www.example.com");

// Return to the previous page
router.back();

// Replace the current page with the specified URL
router.back("https://www.another-example.com");
```

Through the above steps, you can easily perform page navigation and replacement operations in the browser.

## Precautions
- Ensure that the provided URL is valid and follows the Same-Origin Policy to avoid cross-origin issues.
- In some cases, the browser's history may not be sufficient to support the back operation (for example, a single-page application opened directly), in which case calling `router.back()` may not produce the expected effect.
