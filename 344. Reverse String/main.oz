declare Reverse
fun {Reverse Input}
    case Input of Head | Tail then
        {List.flatten [{Reverse Tail} Head]}
    else
        nil
    end
end

declare TestCase1 = "Hello"
declare TestCase2 = "Hannah"

{Browse {Reverse TestCase1}}
{Browse {Reverse TestCase2}}