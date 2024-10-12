declare Solution
fun {Solution Nums K} CountDict CountBucket BucketPopulator TakeKElements in
    CountDict = {NewDictionary}
    CountBucket = {NewArray 1 {List.length Nums} nil}

    proc {BucketPopulator Nums} NewIndex in
        case Nums of First|Rest then
            NewIndex = {Dictionary.condGet CountDict First 0} + 1
            {Dictionary.put CountDict First NewIndex}

            if (NewIndex > 1) then
                {Array.put CountBucket NewIndex-1 {List.subtract {Array.get CountBucket NewIndex-1} First}}
            end
            {Array.put CountBucket NewIndex {List.append {Array.get CountBucket NewIndex} [First]}}
            {BucketPopulator Rest}
        else skip
        end
    end

    fun {TakeKElements Index TopElements} CurrentBucket MoreToPick in
        CurrentBucket = {Array.get CountBucket Index}
        MoreToPick = K-{List.length TopElements}
        if {List.length CurrentBucket} == 0 then
            {List.flatten {TakeKElements Index-1 TopElements}}
        elseif (MoreToPick == {List.length CurrentBucket}) then
            CurrentBucket|TopElements
        elseif (MoreToPick > {List.length CurrentBucket}) then
            {TakeKElements Index-1 {List.flatten CurrentBucket|TopElements}}
        else
            {List.flatten {List.take CurrentBucket MoreToPick}}|TopElements
        end
    end

    {BucketPopulator Nums}
    {List.flatten {TakeKElements {Array.high CountBucket} nil}}
end

declare TestCase1 = [1 1 1 2 2 3]
declare TestCase2 = [1 1 1 1 1 1]
declare TestCase3 = [1 2 2 3 3 3 4 4 4 4 5 5 5 5 5]
declare TestCase4 = [1 1 1 1 1 2 2 2 2 3 3 3 4 4 5]

{Browse {Solution TestCase1 2}} % [2 1]
{Browse {Solution TestCase2 1}} % [1]
{Browse {Solution TestCase3 4}} % [2 3 4 5]
{Browse {Solution TestCase4 2}} % [2 1]