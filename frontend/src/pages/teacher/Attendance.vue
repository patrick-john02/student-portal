<script lang="ts">
export const description = "Teacher attendance monitoring page"
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
  BreadcrumbLink,
  BreadcrumbList,
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
  TableCell,
  TableBody,
} from "@/components/ui/table"

import {
  Calendar,
  UserCheck,
  UserX,
  Clock,
  AlertCircle,
  Search,
  ChevronLeft,
  ChevronRight,
} from "lucide-vue-next"

const userRole = "Teacher"

// Mock student attendance for the day
const attendanceList = ref([
  { id: 1, name: "Carlos Dela Cruz", status: "Present", time: "7:58 AM" },
  { id: 2, name: "Maria Santos", status: "Present", time: "8:01 AM" },
  { id: 3, name: "John Perez", status: "Absent", time: null },
  { id: 4, name: "Angela Ramos", status: "Late", time: "8:27 AM" },
  { id: 5, name: "Mark Rivera", status: "Excused", time: null },
])

const search = ref("")
const date = ref("November 15, 2025")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Attendance</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Title -->
        <div>
          <h2 class="text-2xl font-bold tracking-tight">Attendance Monitoring</h2>
          <p class="text-sm text-muted-foreground">
            Track and manage student attendance for your sections.
          </p>
        </div>

        <!-- Date Navigation -->
        <Card>
          <CardContent class="flex items-center justify-between py-4">
            <div class="flex items-center gap-2">
              <Button variant="outline" size="icon">
                <ChevronLeft class="h-4 w-4" />
              </Button>

              <div class="flex items-center gap-2 font-medium">
                <Calendar class="h-4 w-4 text-primary" />
                {{ date }}
              </div>

              <Button variant="outline" size="icon">
                <ChevronRight class="h-4 w-4" />
              </Button>
            </div>

            <Input
              v-model="search"
              placeholder="Search students..."
              class="max-w-xs"
            />
          </CardContent>
        </Card>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-4">
          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Present</CardTitle>
              <UserCheck class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ attendanceList.filter(a => a.status === 'Present').length }}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Absent</CardTitle>
              <UserX class="h-5 w-5 text-red-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ attendanceList.filter(a => a.status === 'Absent').length }}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Late</CardTitle>
              <Clock class="h-5 w-5 text-orange-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ attendanceList.filter(a => a.status === 'Late').length }}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Excused</CardTitle>
              <AlertCircle class="h-5 w-5 text-purple-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ attendanceList.filter(a => a.status === 'Excused').length }}
              </p>
            </CardContent>
          </Card>
        </div>

        <!-- Attendance Table -->
        <Card>
          <CardHeader>
            <CardTitle>Today's Attendance</CardTitle>
            <CardDescription>
              Review attendance for the selected date.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student Name</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead>Time In</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="student in attendanceList"
                  :key="student.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Student Name -->
                  <TableCell class="font-medium">
                    {{ student.name }}
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="
                        student.status === 'Present'
                          ? 'default'
                          : student.status === 'Absent'
                          ? 'destructive'
                          : student.status === 'Late'
                          ? 'secondary'
                          : 'outline'
                      "
                    >
                      {{ student.status }}
                    </Badge>
                  </TableCell>

                  <!-- Time In -->
                  <TableCell class="text-muted-foreground">
                    {{ student.time || '—' }}
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <Button variant="outline" size="sm">
                      <Search class="h-4 w-4 mr-1" />
                      View
                    </Button>
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
