type Split<T extends string> = T extends `${infer Head}${infer Tail}` ? Head | Split<Tail> : never;

type Numeric = Split<"0123456789">;
type LowerLetter = Split<"abcdefghijklmnopqrstuvwxyz">;
type UpperLetter = Uppercase<LowerLetter>;
type AlphaNumeric = Numeric | LowerLetter | UpperLetter;

type RemoveNonAlphaNumeric<T extends string> = T extends `${infer Head}${infer Tail}`
    ? `${Head extends AlphaNumeric ? Head : ""}${RemoveNonAlphaNumeric<Tail>}`
    : "";

type ReverseString<T extends string> = T extends `${infer Head}${infer Tail}` ? `${ReverseString<Tail>}${Head}` : T;
type IsPalindrome<T extends string> = T extends ReverseString<T> ? true : false;
type Answer<T extends string> = IsPalindrome<Lowercase<RemoveNonAlphaNumeric<T>>>;

function removeNonAlphaNumeric<T extends string>(s: T): RemoveNonAlphaNumeric<T> {
    return s
        .split("")
        .filter((l) => "0123456789abcdefghijklmnopqrstuvyxyz".includes(l.toLowerCase()))
        .join("") as RemoveNonAlphaNumeric<T>;
}

function isPalindrome<T extends string>(s: T): Answer<T> {
    let cleaned = removeNonAlphaNumeric(s).toLowerCase() as Lowercase<RemoveNonAlphaNumeric<T>>;
    return (cleaned.split("").reverse().join("") === cleaned) as IsPalindrome<typeof cleaned>;
}

let isPal: Answer<"A man, a plan, a canal: Panama">; // type: true
let isPal2: Answer<"abc">; // type: false
