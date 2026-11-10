# 🖼️ Fix: Images Not Showing

## Problem
Images aren't showing because the server is running OLD code.

## Solution - Follow These Steps:

### Step 1: STOP the Server
In your terminal, press:
```
CTRL + C
```
Wait until you see the command prompt return.

### Step 2: RESTART the Server
Run this command:
```bash
npm run dev
```

You should see:
```
Opening your browser...
http://localhost:7000
```
(Note: Now on port 7000, not 5000!)

### Step 3: Clear Browser Cache
When the browser opens, press:
- **Windows/Linux:** `CTRL + SHIFT + R`
- **Mac:** `CMD + SHIFT + R`

Or manually:
- Click the refresh button while holding SHIFT

### Step 4: Test the Images
1. Go to **Learn Mode**
2. You should see the JSL hand sign images from `jsl_alphabet_test/`
3. Navigate through letters A-Z

## Still Not Working?

### Check Browser Console:
1. Press `F12` to open developer tools
2. Click "Console" tab
3. Look for any red errors
4. Share the error message with me

### Check Network Tab:
1. Press `F12`
2. Click "Network" tab
3. Refresh the page
4. Look for failed image requests (red)
5. Click on a failed image to see the path

## Expected Behavior:
✅ Images load from: `/src/jsl_alphabet_test/A_test.jpg`
✅ Server runs on: `http://localhost:7000`
✅ All 26 images display correctly

## Quick Test:
Try opening this URL directly in browser:
```
http://localhost:7000/src/jsl_alphabet_test/A_test.jpg
```

If you see the image, the server is working!
If you get an error, the server needs to be restarted.
