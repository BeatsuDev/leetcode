int lengthOfLongestSubstring(char* s) {
    int seenChars[255];
    memset(seenChars, -1, sizeof(seenChars));

    int length = strlen(s);

    int longest = 0;
    int i = 0;
    int j = 0;
    for (; j < length; j++) {
        if (length - i <= longest) break;

        int seenIndex = seenChars[(int) s[j]];
        if (j - i > longest) longest = j - i;
        if (seenIndex >= i) i = seenIndex + 1;

        seenChars[(int) s[j]] = j;
    }

    if (j - i > longest) {
        return j - i;
    }

    return longest;
}