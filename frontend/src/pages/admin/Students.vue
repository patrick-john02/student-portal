<script lang="ts">
export const description = "Student management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed, h } from 'vue'
import {
  useVueTable,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  type ColumnDef,
  type SortingState,
  type ColumnFiltersState,
  FlexRender,
} from '@tanstack/vue-table'
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { 
  Plus, 
  Search, 
  Download, 
  Filter,
  MoreHorizontal,
  Eye,
  Edit,
  Trash2,
  Mail,
  Phone,
  CheckCircle,
  XCircle,
  Users,
  UserCheck,
  GraduationCap,
  ArrowUpDown,
  ChevronLeft,
  ChevronRight,
} from "lucide-vue-next"

const userRole = 'Admin'

// Types
interface Student {
  id: number
  studentId: string
  lrn: string
  name: string
  email: string
  phone: string
  strand: string
  gradeLevel: string
  section: string
  guardianName: string
  guardianContact: string
  enrollmentDate: string
  status: 'active' | 'inactive'
}

// Mock data based on database schema
const students = ref<Student[]>([
  { 
    id: 1, 
    studentId: 'STU-2024-001', 
    lrn: '123456789012',
    name: 'Anna Marie Santos', 
    email: 'anna.santos@student.ucv.edu', 
    phone: '0917-111-2222',
    strand: 'STEM',
    gradeLevel: 'Grade 11',
    section: 'Einstein',
    guardianName: 'Maria Santos',
    guardianContact: '0917-111-3333',
    enrollmentDate: '2024-06-01',
    status: 'active'
  },
  { 
    id: 2, 
    studentId: 'STU-2024-002', 
    lrn: '123456789013',
    name: 'Carlo Miguel Reyes', 
    email: 'carlo.reyes@student.ucv.edu', 
    phone: '0918-222-3333',
    strand: 'ABM',
    gradeLevel: 'Grade 12',
    section: 'Rizal',
    guardianName: 'Roberto Reyes',
    guardianContact: '0918-222-4444',
    enrollmentDate: '2023-06-01',
    status: 'active'
  },
  { 
    id: 3, 
    studentId: 'STU-2024-003', 
    lrn: '123456789014',
    name: 'Sofia Mae Cruz', 
    email: 'sofia.cruz@student.ucv.edu', 
    phone: '0919-333-4444',
    strand: 'HUMSS',
    gradeLevel: 'Grade 11',
    section: 'Bonifacio',
    guardianName: 'Lisa Cruz',
    guardianContact: '0919-333-5555',
    enrollmentDate: '2024-06-01',
    status: 'active'
  },
  { 
    id: 4, 
    studentId: 'STU-2024-004', 
    lrn: '123456789015',
    name: 'Miguel Angelo Garcia', 
    email: 'miguel.garcia@student.ucv.edu', 
    phone: '0920-444-5555',
    strand: 'TVL',
    gradeLevel: 'Grade 12',
    section: 'Mabini',
    guardianName: 'Robert Garcia',
    guardianContact: '0920-444-6666',
    enrollmentDate: '2023-06-01',
    status: 'active'
  },
  { 
    id: 5, 
    studentId: 'STU-2024-005', 
    lrn: '123456789016',
    name: 'Isabella Rose Morales', 
    email: 'isabella.morales@student.ucv.edu', 
    phone: '0921-555-6666',
    strand: 'GAS',
    gradeLevel: 'Grade 11',
    section: 'Luna',
    guardianName: 'Lisa Morales',
    guardianContact: '0921-555-7777',
    enrollmentDate: '2024-06-01',
    status: 'inactive'
  },
  { 
    id: 6, 
    studentId: 'STU-2024-006', 
    lrn: '123456789017',
    name: 'Gabriel Luis Ramos', 
    email: 'gabriel.ramos@student.ucv.edu', 
    phone: '0922-666-7777',
    strand: 'STEM',
    gradeLevel: 'Grade 12',
    section: 'Newton',
    guardianName: 'Pedro Ramos',
    guardianContact: '0922-666-8888',
    enrollmentDate: '2023-06-01',
    status: 'active'
  },
  { 
    id: 7, 
    studentId: 'STU-2024-007', 
    lrn: '123456789018',
    name: 'Samantha Joy Dela Cruz', 
    email: 'samantha.delacruz@student.ucv.edu', 
    phone: '0923-777-8888',
    strand: 'ABM',
    gradeLevel: 'Grade 11',
    section: 'Aquino',
    guardianName: 'Juan Dela Cruz',
    guardianContact: '0923-777-9999',
    enrollmentDate: '2024-06-01',
    status: 'active'
  },
  { 
    id: 8, 
    studentId: 'STU-2024-008', 
    lrn: '123456789019',
    name: 'Ethan James Torres', 
    email: 'ethan.torres@student.ucv.edu', 
    phone: '0924-888-9999',
    strand: 'HUMSS',
    gradeLevel: 'Grade 12',
    section: 'Jacinto',
    guardianName: 'Maria Torres',
    guardianContact: '0924-888-0000',
    enrollmentDate: '2023-06-01',
    status: 'active'
  },
])

// Table state
const sorting = ref<SortingState>([])
const columnFilters = ref<ColumnFiltersState>([])
const globalFilter = ref('')
const selectedStrand = ref('all')
const selectedGrade = ref('all')
const selectedStatus = ref('all')

// Columns definition
const columns: ColumnDef<Student>[] = [
  {
    accessorKey: 'studentId',
    header: 'Student ID',
    cell: ({ row }) => h('div', { class: 'font-medium' }, row.getValue('studentId')),
  },
  {
    accessorKey: 'name',
    header: ({ column }) => {
      return h(Button, {
        variant: 'ghost',
        onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
      }, () => [
        'Name',
        h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })
      ])
    },
    cell: ({ row }) => {
      const student = row.original
      const initials = student.name.split(' ').map(n => n[0]).join('')
      return h('div', { class: 'flex items-center gap-2' }, [
        h('div', { class: 'h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center' }, [
          h('span', { class: 'text-sm font-medium' }, initials)
        ]),
        h('div', {}, [
          h('p', { class: 'font-medium' }, student.name),
          h('p', { class: 'text-xs text-muted-foreground' }, student.lrn)
        ])
      ])
    },
  },
  {
    accessorKey: 'strand',
    header: 'Strand',
    cell: ({ row }) => h(Badge, { variant: 'outline' }, () => row.getValue('strand')),
  },
  {
    accessorKey: 'gradeLevel',
    header: 'Grade Level',
    cell: ({ row }) => h('div', { class: 'text-sm' }, row.getValue('gradeLevel')),
  },
  {
    accessorKey: 'section',
    header: 'Section',
    cell: ({ row }) => h('div', { class: 'text-sm font-medium' }, row.getValue('section')),
  },
  {
    accessorKey: 'guardianName',
    header: 'Guardian',
    cell: ({ row }) => {
      const student = row.original
      return h('div', { class: 'flex flex-col gap-1' }, [
        h('p', { class: 'text-sm' }, student.guardianName),
        h('div', { class: 'flex items-center gap-1 text-xs text-muted-foreground' }, [
          h(Phone, { class: 'h-3 w-3' }),
          h('span', {}, student.guardianContact)
        ])
      ])
    },
  },
  {
    accessorKey: 'email',
    header: 'Contact',
    cell: ({ row }) => {
      const student = row.original
      return h('div', { class: 'flex flex-col gap-1' }, [
        h('div', { class: 'flex items-center gap-1 text-xs text-muted-foreground' }, [
          h(Mail, { class: 'h-3 w-3' }),
          h('span', {}, student.email)
        ]),
        h('div', { class: 'flex items-center gap-1 text-xs text-muted-foreground' }, [
          h(Phone, { class: 'h-3 w-3' }),
          h('span', {}, student.phone)
        ])
      ])
    },
  },
  {
    accessorKey: 'status',
    header: 'Status',
    cell: ({ row }) => {
      const status = row.getValue('status') as string
      const isActive = status === 'active'
      return h(Badge, { variant: isActive ? 'default' : 'secondary' }, () => [
        h(isActive ? CheckCircle : XCircle, { class: 'mr-1 h-3 w-3' }),
        isActive ? 'Active' : 'Inactive'
      ])
    },
  },
  {
    id: 'actions',
    header: () => h('div', { class: 'text-right' }, 'Actions'),
    cell: () => {
      return h('div', { class: 'text-right' }, [
        h(DropdownMenu, {}, {
          default: () => [
            h(DropdownMenuTrigger, { asChild: true }, {
              default: () => h(Button, { variant: 'ghost', size: 'icon' }, {
                default: () => h(MoreHorizontal, { class: 'h-4 w-4' })
              })
            }),
            h(DropdownMenuContent, { align: 'end' }, {
              default: () => [
                h(DropdownMenuLabel, {}, { default: () => 'Actions' }),
                h(DropdownMenuSeparator),
                h(DropdownMenuItem, {}, {
                  default: () => [h(Eye, { class: 'mr-2 h-4 w-4' }), 'View Profile']
                }),
                h(DropdownMenuItem, {}, {
                  default: () => [h(Edit, { class: 'mr-2 h-4 w-4' }), 'Edit Student']
                }),
                h(DropdownMenuItem, {}, {
                  default: () => [h(GraduationCap, { class: 'mr-2 h-4 w-4' }), 'View Grades']
                }),
                h(DropdownMenuItem, {}, {
                  default: () => [h(Mail, { class: 'mr-2 h-4 w-4' }), 'Send Message']
                }),
                h(DropdownMenuSeparator),
                h(DropdownMenuItem, { class: 'text-red-600' }, {
                  default: () => [h(Trash2, { class: 'mr-2 h-4 w-4' }), 'Remove Student']
                }),
              ]
            })
          ]
        })
      ])
    },
  },
]

// Filtered data based on strand, grade level, and status
const filteredData = computed(() => {
  return students.value.filter(student => {
    const matchesStrand = selectedStrand.value === 'all' || student.strand === selectedStrand.value
    const matchesGrade = selectedGrade.value === 'all' || student.gradeLevel === selectedGrade.value
    const matchesStatus = selectedStatus.value === 'all' || student.status === selectedStatus.value
    return matchesStrand && matchesGrade && matchesStatus
  })
})

// Table instance
const table = useVueTable({
  get data() {
    return filteredData.value
  },
  columns,
  getCoreRowModel: getCoreRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
  getSortedRowModel: getSortedRowModel(),
  getFilteredRowModel: getFilteredRowModel(),
  onSortingChange: updaterOrValue => {
    sorting.value = typeof updaterOrValue === 'function' ? updaterOrValue(sorting.value) : updaterOrValue
  },
  onColumnFiltersChange: updaterOrValue => {
    columnFilters.value = typeof updaterOrValue === 'function' ? updaterOrValue(columnFilters.value) : updaterOrValue
  },
  onGlobalFilterChange: updaterOrValue => {
    globalFilter.value = typeof updaterOrValue === 'function' ? updaterOrValue(globalFilter.value) : updaterOrValue
  },
  state: {
    get sorting() {
      return sorting.value
    },
    get columnFilters() {
      return columnFilters.value
    },
    get globalFilter() {
      return globalFilter.value
    },
  },
})

// Stats calculations
const uniqueStrands = computed(() => {
  return new Set(students.value.map(s => s.strand)).size
})

const averagePerSection = computed(() => {
  const sections = new Set(students.value.map(s => s.section)).size
  return sections > 0 ? (students.value.length / sections).toFixed(1) : '0'
})
</script>

<template>
  <SidebarProvider>
    <AppSidebar :user-role="userRole" />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
        <div class="flex items-center gap-2 px-4">
          <SidebarTrigger class="-ml-1" />
          <Separator orientation="vertical" class="mr-2 h-4" />
          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem class="hidden md:block">
                <BreadcrumbLink href="/admin/dashboard">
                  Admin
                </BreadcrumbLink>
              </BreadcrumbItem>
              <BreadcrumbSeparator class="hidden md:block" />
              <BreadcrumbItem>
                <BreadcrumbPage>Students</BreadcrumbPage>
              </BreadcrumbItem>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
      </header>

      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Stats Cards -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Total Students</CardTitle>
              <Users class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ students.length }}</div>
              <p class="text-xs text-muted-foreground">
                +12 from last enrollment
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Active Students</CardTitle>
              <UserCheck class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ students.filter(s => s.status === 'active').length }}</div>
              <p class="text-xs text-muted-foreground">
                {{ Math.round((students.filter(s => s.status === 'active').length / students.length) * 100) }}% of total
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Strands</CardTitle>
              <GraduationCap class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ uniqueStrands }}</div>
              <p class="text-xs text-muted-foreground">
                STEM, ABM, HUMSS, TVL, GAS
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Avg. per Section</CardTitle>
              <Users class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ averagePerSection }}</div>
              <p class="text-xs text-muted-foreground">
                Students per section
              </p>
            </CardContent>
          </Card>
        </div>

        <!-- Students Table -->
        <Card>
          <CardHeader>
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <div>
                <CardTitle>Students List</CardTitle>
                <CardDescription>Manage and view all students in the system</CardDescription>
              </div>
              <div class="flex gap-2">
                <Button variant="outline" size="sm">
                  <Download class="mr-2 h-4 w-4" />
                  Export
                </Button>
                <Button size="sm">
                  <Plus class="mr-2 h-4 w-4" />
                  Add Student
                </Button>
              </div>
            </div>
          </CardHeader>
          <CardContent>
            <!-- Filters -->
            <div class="flex flex-col md:flex-row gap-4 mb-6">
              <div class="relative flex-1">
                <Search class="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                <Input 
                  :model-value="globalFilter"
                  @update:model-value="table.setGlobalFilter"
                  placeholder="Search by name, student ID, or LRN..." 
                  class="pl-8"
                />
              </div>
              <Select v-model="selectedStrand">
                <SelectTrigger class="w-full md:w-[150px]">
                  <SelectValue placeholder="Strand" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Strands</SelectItem>
                  <SelectItem value="STEM">STEM</SelectItem>
                  <SelectItem value="ABM">ABM</SelectItem>
                  <SelectItem value="HUMSS">HUMSS</SelectItem>
                  <SelectItem value="TVL">TVL</SelectItem>
                  <SelectItem value="GAS">GAS</SelectItem>
                </SelectContent>
              </Select>
              <Select v-model="selectedGrade">
                <SelectTrigger class="w-full md:w-[150px]">
                  <SelectValue placeholder="Grade" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Grades</SelectItem>
                  <SelectItem value="Grade 11">Grade 11</SelectItem>
                  <SelectItem value="Grade 12">Grade 12</SelectItem>
                </SelectContent>
              </Select>
              <Select v-model="selectedStatus">
                <SelectTrigger class="w-full md:w-[150px]">
                  <SelectValue placeholder="Status" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Status</SelectItem>
                  <SelectItem value="active">Active</SelectItem>
                  <SelectItem value="inactive">Inactive</SelectItem>
                </SelectContent>
              </Select>
              <Button variant="outline" size="icon">
                <Filter class="h-4 w-4" />
              </Button>
            </div>

            <!-- Table -->
            <div class="rounded-md border">
              <Table>
                <TableHeader>
                  <TableRow v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
                    <TableHead v-for="header in headerGroup.headers" :key="header.id">
                      <FlexRender
                        v-if="!header.isPlaceholder"
                        :render="header.column.columnDef.header"
                        :props="header.getContext()"
                      />
                    </TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  <template v-if="table.getRowModel().rows?.length">
                    <TableRow
                      v-for="row in table.getRowModel().rows"
                      :key="row.id"
                      :data-state="row.getIsSelected() ? 'selected' : undefined"
                    >
                      <TableCell v-for="cell in row.getVisibleCells()" :key="cell.id">
                        <FlexRender
                          :render="cell.column.columnDef.cell"
                          :props="cell.getContext()"
                        />
                      </TableCell>
                    </TableRow>
                  </template>
                  <template v-else>
                    <TableRow>
                      <TableCell :colspan="columns.length" class="h-24 text-center">
                        No results found.
                      </TableCell>
                    </TableRow>
                  </template>
                </TableBody>
              </Table>
            </div>

            <!-- Pagination -->
            <div class="flex items-center justify-between mt-4">
              <p class="text-sm text-muted-foreground">
                Showing <span class="font-medium">{{ table.getState().pagination.pageIndex * table.getState().pagination.pageSize + 1 }}</span> to 
                <span class="font-medium">{{ Math.min((table.getState().pagination.pageIndex + 1) * table.getState().pagination.pageSize, table.getFilteredRowModel().rows.length) }}</span> of 
                <span class="font-medium">{{ table.getFilteredRowModel().rows.length }}</span> students
              </p>
              <div class="flex gap-2">
                <Button 
                  variant="outline" 
                  size="sm"
                  @click="table.previousPage()"
                  :disabled="!table.getCanPreviousPage()"
                >
                  <ChevronLeft class="h-4 w-4 mr-1" />
                  Previous
                </Button>
                <Button 
                  variant="outline" 
                  size="sm"
                  @click="table.nextPage()"
                  :disabled="!table.getCanNextPage()"
                >
                  Next
                  <ChevronRight class="h-4 w-4 ml-1" />
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>