

class InputParser:
    query_alpha = []
    input_clauses = []

    def __init__(self, lines):
        self.parse_lines(lines)

    def process_line(self, line):
        list_elem = line.split('OR')
        list_elem = [item.strip() for item in list_elem]
        return list_elem

    def parse_lines(self, lines):
        # 0
        num_query_alpha = int(lines[0])
        end_query_idx = 1+num_query_alpha
        for idx in range(1, end_query_idx, 1):
            self.query_alpha.append(self.process_line(lines[idx])[0])

        num_clauses = int(lines[end_query_idx])
        end_clause_idx = num_clauses + end_query_idx + 1
        for idx in range(end_query_idx + 1, end_clause_idx, 1):
            self.input_clauses.append(self.process_line(lines[idx]))
