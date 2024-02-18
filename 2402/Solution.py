class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort by start time
        meetings.sort()

        # freeAt[i] = earliest time at which room i is free
        freeAt = [0 for i in range(n)]

        # totalMeetings[i] = num meetings in room i
        totalMeetings = [0 for i in range(n)]

        for start, end in meetings:
            haveFree = False
            candidateTime = inf
            candidateRoom = 0

            # check rooms beginning from lowest
            for i in range(n):
                # found free room for meeting start time
                if freeAt[i] <= start:
                    haveFree = True
                    freeAt[i] = end
                    totalMeetings[i] += 1
                    break

                # get the best candidate room
                # with free time closest to meeting start time
                if candidateTime > freeAt[i]:
                    candidateTime = freeAt[i]
                    candidateRoom = i

            # no free room at meeting start time
            # use best candidate
            if not haveFree:
                # add meeting length to account for late start
                freeAt[candidateRoom] += (end - start)
                totalMeetings[candidateRoom] += 1

        ans = 0
        mostMeetings = totalMeetings[0]
        
        for idx in range(n):
            if totalMeetings[idx] > mostMeetings:
                ans = idx
                mostMeetings = totalMeetings[idx]

        return ans
