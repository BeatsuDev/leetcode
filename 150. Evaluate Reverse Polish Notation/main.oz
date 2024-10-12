declare Tokenize
fun {Tokenize Lexemes}
    case Lexemes of First | Rest then
        if First == [43] then
            operator(type:plus) | {Tokenize Rest}
        elseif First == [45] then
            operator(type:minus) | {Tokenize Rest}
        elseif First == [42] then
            operator(type:multiply) | {Tokenize Rest}
        elseif First == [47] then
            operator(type:divide) | {Tokenize Rest}
        else
            % Leetcode task does integer arithmetic, not floats
            number({String.toInt First}) | {Tokenize Rest}
        end
    else nil
    end
end

declare Interpret
fun {Interpret Tokens} InterpretToken in
    fun {InterpretToken Tokens Stack}
        case Tokens of operator(type:Operation) | RestTokens then
            % The stack grows other way than usual. Index 0 is top element of stack
            case Stack of Second|First|RestStack then
                case Operation of plus then
                    {InterpretToken RestTokens First+Second|RestStack}
                [] minus then
                    {InterpretToken RestTokens First-Second|RestStack}
                [] multiply then
                    {InterpretToken RestTokens First*Second|RestStack}
                [] divide then
                    {InterpretToken RestTokens {Int.'div' First Second}|RestStack}
                end
            end
        [] number(N) | RestTokens then
            {InterpretToken RestTokens N|Stack}
        else
            Stack
        end
    end
    {InterpretToken Tokens nil}
end

declare Solution
fun {Solution Input}
    case {Interpret {Tokenize Input}} of N|_ then N else nil end
end

declare TestCase1
declare TestCase2
declare TestCase3

TestCase1 = ["2" "1" "+" "3" "*"]  % 9
TestCase2 = ["4" "13" "5" "/" "+"]  % 6
TestCase3 = ["10" "6" "9" "3" "+" "-11" "*" "/" "*" "17" "+" "5" "+"]  % 22

{Browse {Solution TestCase1}}
{Browse {Solution TestCase2}}
{Browse {Solution TestCase3}}