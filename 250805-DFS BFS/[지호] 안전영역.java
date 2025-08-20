
public class 안전영역 {
    // 주어진 숫자 5 => 5 아래로 잠김

    // DFS 끝나면 돌아오게끔
    boolean[][] visited;
    int N;
    int[] dx = { -1, 0, 1, 0 };
    int[] dy = { 0, 1, 0, -1 };
    int[][] map;
    int count;
    int max;

    public int dfs(int N, int[][] place){
        visited = new boolean[N][N];
        map = place;

        // 최대 N -> N부터 시작해서 내려올 때마다 dfs 의 값을 산출 

        // 최대 값을 구함 
        // 1. 최대 값에서 -1 을 빼면서 for 문 => 받아온 값을 max 해서 최대값으로 교체 
        // 2. 거기서 이중 for문 - 원래대로 
        // 3. 다시 bfs - 원래대로 

        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(vis)


            }
        }



        return 0;
    }

}
