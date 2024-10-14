declare BinarySearch
fun {BinarySearch SortedList Target} RecursiveSearch in
    fun {RecursiveSearch SortedList Start End} MiddleIndex MiddleValue in
        if End - Start == 0 then
            if {List.nth SortedList Start} == Target then Start else ~1 end
        else
            MiddleIndex = {Int.'div' Start+End 2}
            MiddleValue = {List.nth SortedList MiddleIndex}
            if MiddleValue > Target then
                {RecursiveSearch SortedList Start MiddleIndex-1}
            elseif MiddleValue < Target then
                {RecursiveSearch SortedList MiddleIndex+1 End}
            else
                MiddleIndex
            end
        end
    end
    {RecursiveSearch SortedList 1 {List.length SortedList}}
end


declare TestCase1 = [~1 0 3 5 9 12]
declare TestCase2 = [~5 ~4 ~3 ~2 ~1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]

{Browse {BinarySearch TestCase1 9}}
{Browse {BinarySearch TestCase1 2}}
{Browse {BinarySearch TestCase2 10}}