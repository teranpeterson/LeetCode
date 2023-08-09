# WORKING

class Solution:
    def videoStitching(self, clips, T):
        used = []

        prev = -1
        find = 0
        i = 0
        while True:
            print("prev=" + str(prev))
            print("find=" + str(find))
            print()
            max = 0
            choice = None
            for clip in clips:
                if clip[0] > prev and clip[0] <= find and clip[1] > find:
                    l = clip[1] - clip[0]
                    if l > max:
                        max = l
                        choice = clip
            if not choice:
                return -1
            print(choice)
            used.append(choice)
            prev = choice[0]
            find = choice[1]
            if T >= prev and T <= find:
                break
        print(used)

        for i in range(1, len(used) - 1):
            try:
                if used[i-1][1] > used[i][0] and used[i][1] > used[i+1][0] and used[i-1][1] >= used[i+1][0]:
                    del used[i]
            except IndexError:
                break

        print(used)
        return len(used)
        

#          X           X      X               
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
T = 10
# Output: 3

# clips = [[0,1],[1,2]]
# T = 5
# Output: -1
#                                  X                       X                                         X
# clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
# T = 9
# Output: 3

clips = [[0,4],[2,8]]
T = 5
# Output: 2


s = Solution()
print("Solution: " + str(s.videoStitching(clips, T)))






# You are given a series of video clips from a sporting event that lasted T seconds.  
# These video clips can be overlapping with each other and have varied lengths.
# Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends 
# at time clips[i][1].  We can cut these clips into segments freely: for example, 
# a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
# Return the minimum number of clips needed so that we can cut the clips into 
# segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

# Note:
#   1 <= clips.length <= 100
#   0 <= clips[i][0], clips[i][1] <= 100
#   0 <= T <= 100