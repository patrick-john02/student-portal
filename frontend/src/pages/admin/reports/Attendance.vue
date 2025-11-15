<script lang="ts">
export const description = "Attendance reports page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuItem,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import {
  Calendar,
  User,
  MoreHorizontal,
  FileDown,
  Printer,
  Check,
  X,
  Clock,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy attendance data
const attendanceLogs = ref([
  {
    id: 1,
    student: "John Mark Rivera",
    grade: "Grade 11 – STEM A",
    date: "2024-01-12",
    status: "Present",
    time: "07:58 AM",
    color: "bg-green-500",
    remarks: "On time",
  },
  {
    id: 2,
    student: "Andrea Lopez",
    grade: "Grade 11 – HUMSS B",
    date: "2024-01-12",
    status: "Absent",
    time: "--",
    color: "bg-red-500",
    remarks: "Sick leave",
  },
  {
    id: 3,
    student: "Rico Delos Santos",
    grade: "Grade 12 – ABM A",
    date: "2024-01-12",
    status: "Late",
    time: "08:21 AM",
    color: "bg-yellow-500",
    remarks: "Traffic delay",
  },
  {
    id: 4,
    student: "Kyla Francisco",
    grade: "Grade 12 – GAS C",
    date: "2024-01-12",
    status: "Present",
    time: "07:50 AM",
    color: "bg-green-500",
    remarks: "On time",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/reports">Reports</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Attendance Reports</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Attendance Reports</h2>
            <p class="text-sm text-muted-foreground">
              View daily attendance and presence logs of students.
            </p>
          </div>

          <div class="flex gap-2">
            <Button variant="secondary" class="flex items-center gap-2">
              <Printer class="h-4 w-4" />
              Print
            </Button>

            <Button class="flex items-center gap-2">
              <FileDown class="h-4 w-4" />
              Export CSV
            </Button>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Attendance Logs</CardTitle>
            <CardDescription>
              Filter and review attendance per day or per student.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search student..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student</TableHead>
                  <TableHead>Grade & Section</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead>Time</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead>Remarks</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="log in attendanceLogs"
                  :key="log.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Student -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <User class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ log.student }}</span>
                    </div>
                  </TableCell>

                  <!-- Grade -->
                  <TableCell class="text-muted-foreground">
                    {{ log.grade }}
                  </TableCell>

                  <!-- Date -->
                  <TableCell>
                    <div class="flex items-center gap-1">
                      <Calendar class="h-3 w-3 text-muted-foreground" />
                      <span>{{ log.date }}</span>
                    </div>
                  </TableCell>

                  <!-- Time -->
                  <TableCell>
                    <div class="flex items-center gap-1 text-muted-foreground">
                      <Clock class="h-3 w-3" />
                      <span>{{ log.time }}</span>
                    </div>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="
                        log.status === 'Present'
                          ? 'default'
                          : log.status === 'Late'
                          ? 'secondary'
                          : 'destructive'
                      "
                    >
                      <!-- icon -->
                      <span class="flex items-center gap-1">
                        <component
                          :is="
                            log.status === 'Present'
                              ? Check
                              : log.status === 'Late'
                              ? Clock
                              : X
                          "
                          class="h-3 w-3"
                        />
                        {{ log.status }}
                      </span>
                    </Badge>
                  </TableCell>

                  <!-- Remarks -->
                  <TableCell class="text-muted-foreground">
                    {{ log.remarks }}
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button size="icon" variant="ghost">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>View Details</DropdownMenuItem>
                        <DropdownMenuItem>Print Record</DropdownMenuItem>
                        <DropdownMenuItem>Download PDF</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Flag for Review
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
