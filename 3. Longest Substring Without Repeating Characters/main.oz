declare Solution
fun {Solution Input} PointerIterator in
    fun {PointerIterator Left Right Seen Longest}
        if Right > {List.length Input} then
            {Max Right-Left Longest}
        elseif {Dictionary.member Seen {List.nth Input Right}} then
            {PointerIterator {Dictionary.get Seen {List.nth Input Right}}+1 {Dictionary.get Seen {List.nth Input Right}}+1 {NewDictionary} {Max Right-Left Longest}}
        else
            {Dictionary.put Seen {List.nth Input Right} Right}
            {PointerIterator Left Right+1 Seen Longest}
        end
    end

    {PointerIterator 1 1 {NewDictionary} 0}
end

declare TestCase1 = "abcabcbb"
declare TestCase2 = "bbbbb"
declare TestCase3 = "pwwkew"
declare TestCase4 = "aaabcdefg"

{Browse {Solution TestCase1}}
{Browse {Solution TestCase2}}
{Browse {Solution TestCase3}}
{Browse {Solution TestCase4}}