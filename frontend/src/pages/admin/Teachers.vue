<script lang="ts">
export const description = "Teacher management page"
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
  GraduationCap,
  Users,
  ArrowUpDown,
  ChevronLeft,
  ChevronRight,
} from "lucide-vue-next"

const userRole = 'Admin'

// Types
interface Teacher {
  id: number
  employeeId: string
  name: string
  email: string
  phone: string
  specialization: string
  department: string
  subjects: number
  sections: number
  hireDate: string
  status: 'active' | 'inactive'
}

// Mock data
const teachers = ref<Teacher[]>([
  { 
    id: 1, 
    employeeId: 'EMP-001', 
    name: 'Maria Santos', 
    email: 'maria.santos@ucv.edu', 
    phone: '0917-123-4567',
    specialization: 'Mathematics',
    department: 'STEM',
    subjects: 5,
    sections: 3,
    hireDate: '2020-06-15',
    status: 'active'
  },
  { 
    id: 2, 
    employeeId: 'EMP-002', 
    name: 'Juan Dela Cruz', 
    email: 'juan.delacruz@ucv.edu', 
    phone: '0918-234-5678',
    specialization: 'English',
    department: 'HUMSS',
    subjects: 4,
    sections: 4,
    hireDate: '2019-08-20',
    status: 'active'
  },
  { 
    id: 3, 
    employeeId: 'EMP-003', 
    name: 'Ana Reyes', 
    email: 'ana.reyes@ucv.edu', 
    phone: '0919-345-6789',
    specialization: 'Accountancy',
    department: 'ABM',
    subjects: 3,
    sections: 2,
    hireDate: '2021-01-10',
    status: 'active'
  },
  { 
    id: 4, 
    employeeId: 'EMP-004', 
    name: 'Robert Garcia', 
    email: 'robert.garcia@ucv.edu', 
    phone: '0920-456-7890',
    specialization: 'Physical Education',
    department: 'GAS',
    subjects: 6,
    sections: 5,
    hireDate: '2018-03-05',
    status: 'active'
  },
  { 
    id: 5, 
    employeeId: 'EMP-005', 
    name: 'Lisa Morales', 
    email: 'lisa.morales@ucv.edu', 
    phone: '0921-567-8901',
    specialization: 'Culinary Arts',
    department: 'TVL',
    subjects: 4,
    sections: 3,
    hireDate: '2022-07-12',
    status: 'inactive'
  },
  { 
    id: 6, 
    employeeId: 'EMP-006', 
    name: 'Pedro Ramos', 
    email: 'pedro.ramos@ucv.edu', 
    phone: '0922-678-9012',
    specialization: 'Biology',
    department: 'STEM',
    subjects: 5,
    sections: 4,
    hireDate: '2020-09-01',
    status: 'active'
  },
  { 
    id: 7, 
    employeeId: 'EMP-007', 
    name: 'Sofia Cruz', 
    email: 'sofia.cruz@ucv.edu', 
    phone: '0923-789-0123',
    specialization: 'History',
    department: 'HUMSS',
    subjects: 3,
    sections: 3,
    hireDate: '2021-05-15',
    status: 'active'
  },
])

// Table state
const sorting = ref<SortingState>([])
const columnFilters = ref<ColumnFiltersState>([])
const globalFilter = ref('')
const selectedDepartment = ref('all')
const selectedStatus = ref('all')

// Columns definition
const columns: ColumnDef<Teacher>[] = [
  {
    accessorKey: 'employeeId',
    header: 'Employee ID',
    cell: ({ row }) => h('div', { class: 'font-medium' }, row.getValue('employeeId')),
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
      const teacher = row.original
      const initials = teacher.name.split(' ').map(n => n[0]).join('')
      return h('div', { class: 'flex items-center gap-2' }, [
        h('div', { class: 'h-8 w-8 rounded-full bg-primary/10 flex items-center justify-center' }, [
          h('span', { class: 'text-sm font-medium' }, initials)
        ]),
        h('div', {}, [
          h('p', { class: 'font-medium' }, teacher.name),
          h('p', { class: 'text-xs text-muted-foreground' }, teacher.email)
        ])
      ])
    },
  },
  {
    accessorKey: 'department',
    header: 'Department',
    cell: ({ row }) => h(Badge, { variant: 'outline' }, () => row.getValue('department')),
  },
  {
    accessorKey: 'specialization',
    header: 'Specialization',
    cell: ({ row }) => h('div', { class: 'text-sm' }, row.getValue('specialization')),
  },
  {
    accessorKey: 'subjects',
    header: () => h('div', { class: 'text-center' }, 'Subjects'),
    cell: ({ row }) => h('div', { class: 'text-center' }, row.getValue('subjects')),
  },
  {
    accessorKey: 'sections',
    header: () => h('div', { class: 'text-center' }, 'Sections'),
    cell: ({ row }) => h('div', { class: 'text-center' }, row.getValue('sections')),
  },
  {
    accessorKey: 'phone',
    header: 'Contact',
    cell: ({ row }) => {
      const teacher = row.original
      return h('div', { class: 'flex flex-col gap-1' }, [
        h('div', { class: 'flex items-center gap-1 text-xs text-muted-foreground' }, [
          h(Phone, { class: 'h-3 w-3' }),
          h('span', {}, teacher.phone)
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
                  default: () => [h(Eye, { class: 'mr-2 h-4 w-4' }), 'View Details']
                }),
                h(DropdownMenuItem, {}, {
                  default: () => [h(Edit, { class: 'mr-2 h-4 w-4' }), 'Edit Teacher']
                }),
                h(DropdownMenuItem, {}, {
                  default: () => [h(Mail, { class: 'mr-2 h-4 w-4' }), 'Send Message']
                }),
                h(DropdownMenuSeparator),
                h(DropdownMenuItem, { class: 'text-red-600' }, {
                  default: () => [h(Trash2, { class: 'mr-2 h-4 w-4' }), 'Remove Teacher']
                }),
              ]
            })
          ]
        })
      ])
    },
  },
]

// Filtered data based on department and status
const filteredData = computed(() => {
  return teachers.value.filter(teacher => {
    const matchesDept = selectedDepartment.value === 'all' || teacher.department === selectedDepartment.value
    const matchesStatus = selectedStatus.value === 'all' || teacher.status === selectedStatus.value
    return matchesDept && matchesStatus
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
                <BreadcrumbPage>Teachers</BreadcrumbPage>
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
              <CardTitle class="text-sm font-medium">Total Teachers</CardTitle>
              <GraduationCap class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ teachers.length }}</div>
              <p class="text-xs text-muted-foreground">
                +3 from last semester
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Active Teachers</CardTitle>
              <CheckCircle class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ teachers.filter(t => t.status === 'active').length }}</div>
              <p class="text-xs text-muted-foreground">
                {{ Math.round((teachers.filter(t => t.status === 'active').length / teachers.length) * 100) }}% of total
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Departments</CardTitle>
              <Users class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">5</div>
              <p class="text-xs text-muted-foreground">
                STEM, ABM, HUMSS, TVL, GAS
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Avg. Load</CardTitle>
              <GraduationCap class="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">{{ (teachers.reduce((sum, t) => sum + t.subjects, 0) / teachers.length).toFixed(1) }}</div>
              <p class="text-xs text-muted-foreground">
                Subjects per teacher
              </p>
            </CardContent>
          </Card>
        </div>

        <!-- Teachers Table -->
        <Card>
          <CardHeader>
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <div>
                <CardTitle>Teachers List</CardTitle>
                <CardDescription>Manage and view all teachers in the system</CardDescription>
              </div>
              <div class="flex gap-2">
                <Button variant="outline" size="sm">
                  <Download class="mr-2 h-4 w-4" />
                  Export
                </Button>
                <Button size="sm">
                  <Plus class="mr-2 h-4 w-4" />
                  Add Teacher
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
                  placeholder="Search by name, email, or employee ID..." 
                  class="pl-8"
                />
              </div>
              <Select v-model="selectedDepartment">
                <SelectTrigger class="w-full md:w-[180px]">
                  <SelectValue placeholder="Department" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Departments</SelectItem>
                  <SelectItem value="STEM">STEM</SelectItem>
                  <SelectItem value="ABM">ABM</SelectItem>
                  <SelectItem value="HUMSS">HUMSS</SelectItem>
                  <SelectItem value="TVL">TVL</SelectItem>
                  <SelectItem value="GAS">GAS</SelectItem>
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
                <span class="font-medium">{{ table.getFilteredRowModel().rows.length }}</span> teachers
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