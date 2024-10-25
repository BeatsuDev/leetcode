declare Solution
fun {Solution Input} InnerLoop in
    fun {InnerLoop Left Right LargestSoFar} CurrentContainerSize in
        if Left < Right then
            CurrentContainerSize = {Min {List.nth Input Left} {List.nth Input Right}} * (Right - Left)
            if {List.nth Input Left} < {List.nth Input Right} then
                {InnerLoop Left+1 Right {Max LargestSoFar CurrentContainerSize}}
            else
                {InnerLoop Left Right-1 {Max LargestSoFar CurrentContainerSize}}
            end
        else
            LargestSoFar
        end
    end

    {InnerLoop 1 {List.length Input} 0}
end


declare TestCase1 = [1 8 6 2 5 4 8 3 7]  % Correct answer: 49
declare TestCase2 = [1 1]  % Correct answer: 1

{Browse {Solution TestCase1}}
{Browse {Solution TestCase2}}