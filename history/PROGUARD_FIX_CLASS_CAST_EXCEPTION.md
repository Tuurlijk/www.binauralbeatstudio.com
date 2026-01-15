# Fix ClassCastException in Release Build - ProGuard Keep Rules

## Problem

The release build crashes with `ClassCastException: eg.n cannot be cast to jh.g` when previewing or reloading samplepacks. This occurs in:

- `NativeMindStateEngine$SessionDataBuilder.build` at line 286
- Affects both `ACTION_PREVIEW_PLAY` and `ACTION_PREVIEW_RELOAD`

## Root Cause

ProGuard/R8 obfuscation is renaming classes that need to maintain their type information for casting operations. The obfuscated class names (`eg.n` and `jh.g`) indicate that type information is being lost during minification.

## Solution

Add ProGuard keep rules to preserve the necessary classes and their type information. The fix needs to be applied to the Android project's ProGuard configuration file (typically `proguard-rules.pro` in the `app` module).

### Required ProGuard Rules

Add the following rules to `app/proguard-rules.pro`:

```proguard
# Keep NativeMindStateEngine and SessionDataBuilder classes
-keep class com.michielroos.mindstate.native.NativeMindStateEngine { *; }
-keep class com.michielroos.mindstate.native.NativeMindStateEngine$SessionDataBuilder { *; }

# Keep all methods in SessionDataBuilder, especially build()
-keepclassmembers class com.michielroos.mindstate.native.NativeMindStateEngine$SessionDataBuilder {
    <methods>;
    <fields>;
}

# Keep classes used in SessionDataBuilder.build() that might be cast
# Based on the error, there's likely a collection or data structure being cast
-keep class com.michielroos.mindstate.native.** { *; }

# If SessionDataBuilder uses generics or collections, keep those too
-keepclassmembers class * {
    <fields>;
}

# Keep all native methods (if any)
-keepclasseswithmembernames class * {
    native <methods>;
}
```

### More Specific Fix (if above doesn't work)

If the issue persists, the problem might be with specific data types being passed. Check the `SessionDataBuilder.build()` method implementation to identify what types are being cast. Then add more specific rules:

```proguard
# Example: If it's a List or Collection issue
-keep class java.util.** { *; }
-keep interface java.util.** { *; }

# Example: If it's a custom data class
-keep class com.michielroos.mindstate.model.** { *; }
-keep class com.michielroos.mindstate.data.** { *; }
```

### Verification Steps

1. Add the ProGuard rules to `app/proguard-rules.pro`
2. Build a release APK/AAB: `./gradlew assembleRelease` or `./gradlew bundleRelease`
3. Install the release build on a device
4. Test samplepack preview functionality
5. Test samplepack reload functionality
6. Verify no ClassCastException occurs

### Alternative: Disable Obfuscation for Native Classes (Temporary)

If the above doesn't work immediately, you can temporarily disable obfuscation for the native package to identify the exact classes involved:

```proguard
-keep class com.michielroos.mindstate.native.** { *; }
-dontobfuscate com.michielroos.mindstate.native.**
```

Then gradually narrow down which specific classes need to be kept.

## Implementation Location

The ProGuard rules should be added to:
- `app/proguard-rules.pro` (main app module)
- Or referenced in `app/build.gradle` if using a different location

Example in `app/build.gradle`:
```gradle
android {
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

## Related Files to Check

1. `app/proguard-rules.pro` - Main ProGuard configuration
2. `app/src/main/java/com/michielroos/mindstate/native/NativeMindStateEngine.java` - Source file with SessionDataBuilder
3. `app/src/main/java/com/michielroos/mindstate/native/NativeMindStateEngine.kt` - Kotlin file calling loadSession
4. `app/src/main/java/com/michielroos/mindstate/services/MindStateService.kt` - Service handling preview actions

## Notes

- The error occurs at line 286 in `SessionDataBuilder.build()`, so check that specific line to see what cast operation is failing
- The obfuscated names (`eg.n`, `jh.g`) suggest these are inner classes or nested types
- Consider using `-keepattributes Signature` to preserve generic type information if generics are involved
- Consider using `-keepattributes Exceptions` if exception handling is affected
