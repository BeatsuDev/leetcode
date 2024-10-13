declare Solution
fun {Solution Input} Pairs Inner in
    Pairs = brackets(&(:&) &[:&] &{:&})
    fun {Inner Brackets OpeningStack}
        case Brackets of Bracket|InputTail then
            if {List.member Bracket ")]}" } then
                case OpeningStack of OpeningBracket|StackTail then
                    if Pairs.!OpeningBracket == Bracket then
                        {Inner InputTail StackTail}
                    else
                        OpeningStack
                    end
                end
            else
                {Inner InputTail Bracket|OpeningStack}
            end
        else
            OpeningStack
        end
    end
    {List.length {Inner Input nil}} == 0
end

declare TestCase1 = "()"
declare TestCase2 = "()[]{}"
declare TestCase3 = "(]"
declare TestCase4 = "([])"
declare TestCase5 = "(()"

{Browse {Solution TestCase1}}
{Browse {Solution TestCase2}}
{Browse {Solution TestCase3}}
{Browse {Solution TestCase4}}
{Browse {Solution TestCase5}}