import typing

Grid = typing.NewType("Grid", typing.List[typing.List[str]])
Location = typing.NewType("Location", typing.Tuple[int, int])


class Region:
    def __init__(self, locations: set, crop_type: str, containing_region_location: typing.Optional[Location]):
        self.__locations: set = locations
        self.__crop_type: str = crop_type
        self.containing_region_location: Location = containing_region_location
        self.__outer_perimeter: int = 0
        self.__inner_perimeter: int = 0

    def is_location_in_region(self, location: Location) -> bool:
        return location in self.__locations

    def __get_area(self) -> int:
        return len(self.__locations)

    def get_perimeter_location(self) -> Location:
        row_inside, col_inside = None, None
        max_row = 0
        for row, col in self.__locations:
            if row > max_row:
                row_inside, col_inside = row, col
                max_row = row
        return Location((row_inside, col_inside))

    def walk_outer_perimeter(self) -> None:
        row_inside, col_inside = self.get_perimeter_location()

        row_outside, col_outside = None, None
        for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            candidate = row_inside + delta_row, col_inside + delta_col
            if candidate not in self.__locations:
                row_outside, col_outside = candidate
                break

        start_location_inside = row_inside, col_inside
        start_location_outside = row_outside, col_outside
        prev_location_inside = None
        prev_location_outside = None

        n_sides = 0
        while True:
            did_take_step = False
            for step_option in ("straight", "outside_corner", "inside_corner"):
                for delta in (1, -1):
                    if step_option == "straight":
                        if row_inside == row_outside:
                            row_step = delta
                            col_step = 0
                        else:
                            row_step = 0
                            col_step = delta
                        candidate_inside = row_inside + row_step, col_inside + col_step
                        candidate_outside = row_outside + row_step, col_outside + col_step
                    elif step_option == "outside_corner":
                        candidate_inside = row_inside, col_inside
                        if row_inside == row_outside:
                            candidate_outside = row_inside + delta, col_inside
                            if (row_inside + delta, col_outside) in self.__locations:
                                continue
                        else:
                            candidate_outside = row_inside, col_inside + delta
                            if (row_outside, col_inside + delta) in self.__locations:
                                continue
                    else:
                        candidate_outside = row_outside, col_outside
                        if row_inside == row_outside:
                            candidate_inside = row_outside + delta, col_outside
                        else:
                            candidate_inside = row_outside, col_outside + delta

                    if (candidate_inside in self.__locations) and \
                       (candidate_outside not in self.__locations) and \
                       (not ((candidate_inside == prev_location_inside) and (candidate_outside == prev_location_outside))):
                        if (candidate_inside == start_location_inside) and (candidate_outside == start_location_outside):
                            if step_option != "straight":
                                n_sides += 1
                            self.__outer_perimeter = n_sides
                            return
                        prev_location_inside = row_inside, col_inside
                        prev_location_outside = row_outside, col_outside
                        row_inside, col_inside = candidate_inside
                        row_outside, col_outside = candidate_outside
                        did_take_step = True
                        break
                if did_take_step:
                    if step_option != "straight":
                        n_sides += 1
                    break

    def get_outer_perimeter(self) -> int:
        return self.__outer_perimeter

    def add_inner_perimeter(self, inner_perimeter: int) -> None:
        self.__inner_perimeter += inner_perimeter

    def get_price(self) -> int:
        return self.__get_area() * (self.get_outer_perimeter() + self.__inner_perimeter)


def find_new_region_start(points_processed, grid: Grid):
    n_rows, n_cols = len(grid), len(grid[0])
    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            if (row, col) not in points_processed:
                points_processed.add((row, col))
                return row, col
    return None


def walk_next_region(points_processed, grid: Grid):
    row, col = find_new_region_start(points_processed, grid)
    crop_type = grid[row][col]
    adjacent_crop_types = set()
    adjacent_crop_location = None
    new_region = {(row, col)}
    frontier = {(row, col)}
    while True:
        frontier_next = set()
        for row, col in frontier:
            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                candidate = row + delta_row, col + delta_col
                this_crop_type = grid[row + delta_row][col + delta_col]
                if (crop_type == this_crop_type) and (candidate not in points_processed):
                    points_processed.add(candidate)
                    frontier_next.add(candidate)
                    new_region.add(candidate)
                elif crop_type != this_crop_type:
                    adjacent_crop_types.add(this_crop_type)
                    adjacent_crop_location = candidate
        if len(frontier_next) == 0:
            break
        frontier = frontier_next

    if len(adjacent_crop_types) != 1:
        adjacent_crop_location = None

    return Region(new_region, crop_type, adjacent_crop_location)


def get_region_from_location(regions: typing.List[Region], location: Location):
    for region in regions:
        if region.is_location_in_region(location):
            return region
    return None


grid = []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        grid.append(["."] + [char for char in line] + ["."])

grid = [["."] * len(grid[0])] + grid + [["."] * len(grid[0])]
n_rows, n_cols = len(grid), len(grid[0])
grid = Grid(grid)

points_processed = set()
regions = []
while len(points_processed) < ((n_rows - 2) * (n_cols - 2)):
    new_region = walk_next_region(points_processed, grid)
    regions.append(new_region)

for region in regions:
    region.walk_outer_perimeter()

for region in regions:
    containing_region_location = region.containing_region_location
    if containing_region_location is not None:
        containing_region = get_region_from_location(regions, containing_region_location)
        containing_region.add_inner_perimeter(region.get_outer_perimeter())

total_fencing_price = 0
for region in regions:
    total_fencing_price += region.get_price()
print(total_fencing_price)
