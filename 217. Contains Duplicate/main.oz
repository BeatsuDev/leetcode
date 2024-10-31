declare Solution
fun {Solution Input} Inner in
    fun {Inner Characters Seen}
        case Characters of Head|Tail then
            if {List.member Head Seen} then
                true
            else
                {Inner Tail Head|Seen}                
            end
        else
            false
        end
    end
    {Inner Input nil}
end



declare TestCase1 = [1 2 3 1]
declare TestCase2 = [1 2 3 4]
declare TestCase3 = [1 1 1 3 3 4 3 2 4 2]

{Browse {Solution TestCase1}}
{Browse {Solution TestCase2}}
{Browse {Solution TestCase3}}