from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Cria um mapa (dicionário) onde cada curso tem uma lista de pré-requisitos
        pre_map = {i: [] for i in range(numCourses)}
        
        # Popula o mapa de pré-requisitos com base na lista fornecida
        for course, prerequesite in prerequisites:
            pre_map[course].append(prerequesite)
        
        # Conjunto para rastrear cursos que estão sendo visitados no momento (detecta ciclos)
        visit_set = set()

        # Função para realizar uma busca em profundidade (DFS)
        def dfs(course):
            # Se o curso já estiver no conjunto de visitados, há um ciclo
            if course in visit_set:
                return False
            # Se o curso não tiver pré-requisitos, ele pode ser concluído
            if pre_map[course] == []:
                return True
            
            # Marca o curso como visitado
            visit_set.add(course)
            
            # Para cada pré-requisito do curso atual, realiza a DFS
            for prerequisite in pre_map[course]:
                # Se a DFS retornar False, há um ciclo e não é possível concluir os cursos
                if not dfs(prerequisite):
                    return False
            
            # Remove o curso do conjunto de visitados (finaliza a DFS para este curso)
            visit_set.remove(course)
            # Marca o curso como "sem pré-requisitos" para evitar trabalho redundante no futuro
            pre_map[course] = []
            
            return True

        # Verifica cada curso para garantir que todos possam ser concluídos
        for course in range(numCourses):
            # Se qualquer DFS retornar False, não é possível concluir todos os cursos
            if not dfs(course):
                return False
        return True



# Method dfs
# Time complexy: O(n + p)

sol = Solution()
print(sol.canFinish(2, [[0, 1], [1, 0]]))