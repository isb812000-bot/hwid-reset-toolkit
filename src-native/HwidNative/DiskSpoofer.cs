using System;

namespace HwidNative;

public static class DiskSpoofer
{
    public static string ReadSerial(int index)
    {
        // placeholder until IOCTL_SMART_GET_VERSION wired up
        return "UNKNOWN";
    }

    public static void WriteSerial(int index, string value)
    {
        if (string.IsNullOrWhiteSpace(value))
            throw new ArgumentException("value required", nameof(value));
        // TODO: IOCTL_DISK_SET_DRIVE_LAYOUT_EX path, gated on admin token
    }
}