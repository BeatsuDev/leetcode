declare TestCase1
declare TestCase2
declare TestCase3
TestCase1 = [2 7 11 15]
TestCase2 = [3 2 4]
TestCase3 = [3 3]

declare TwoSum
fun {TwoSum Numbers Target} Seen I RecursiveFinder in
    fun {RecursiveFinder Numbers Target Seen I}
        case Numbers of N | Rest then
            if {Dictionary.member Seen Target-N} then
                {Dictionary.get Seen Target-N}#I
            else
                {Dictionary.put Seen N I}
                {RecursiveFinder Rest Target Seen I+1}
            end
        else
            ~1#~1
        end
    end
    {RecursiveFinder Numbers Target {NewDictionary} 0}
end

{Browse {TwoSum TestCase1 9}}
{Browse {TwoSum TestCase2 6}}
{Browse {TwoSum TestCase3 6}}