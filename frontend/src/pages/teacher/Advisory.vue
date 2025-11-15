<script lang="ts">
export const description = "Teacher advisory class page"
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

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Separator } from "@/components/ui/separator"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

import {
  Users,
  GraduationCap,
  UserCheck,
  Clock,
  AlertCircle,
  ChevronRight,
} from "lucide-vue-next"

const userRole = "Teacher"

// Advisory class info
const advisoryInfo = {
  section: "STEM 11-A",
  adviser: "Mr. Johnson",
  totalStudents: 45,
  presentToday: 41,
  avgGrade: 87.4,
}

// Students List
const students = ref([
  { id: 1, name: "Carlos Dela Cruz", gender: "Male", status: "Present", grade: 89 },
  { id: 2, name: "Maria Santos", gender: "Female", status: "Present", grade: 92 },
  { id: 3, name: "John Perez", gender: "Male", status: "Absent", grade: 85 },
  { id: 4, name: "Angela Ramos", gender: "Female", status: "Late", grade: 88 },
  { id: 5, name: "Mark Rivera", gender: "Male", status: "Present", grade: 90 },
])

const search = ref("")
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
              <BreadcrumbPage>Advisory Class</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div>
          <h2 class="text-2xl font-bold tracking-tight">Advisory Class</h2>
          <p class="text-sm text-muted-foreground">
            Manage your advisory section, monitor attendance, and track performance.
          </p>
        </div>

        <!-- Section Overview -->
        <Card>
          <CardHeader>
            <CardTitle>{{ advisoryInfo.section }}</CardTitle>
            <CardDescription>Class Overview</CardDescription>
          </CardHeader>
          <CardContent>
            <div class="grid gap-4 md:grid-cols-4">
              <div class="rounded-lg border p-4 flex items-center gap-3">
                <Users class="h-6 w-6 text-primary" />
                <div>
                  <p class="text-sm text-muted-foreground">Total Students</p>
                  <p class="font-semibold text-lg">{{ advisoryInfo.totalStudents }}</p>
                </div>
              </div>

              <div class="rounded-lg border p-4 flex items-center gap-3">
                <UserCheck class="h-6 w-6 text-green-500" />
                <div>
                  <p class="text-sm text-muted-foreground">Present Today</p>
                  <p class="font-semibold text-lg">{{ advisoryInfo.presentToday }}</p>
                </div>
              </div>

              <div class="rounded-lg border p-4 flex items-center gap-3">
                <GraduationCap class="h-6 w-6 text-blue-500" />
                <div>
                  <p class="text-sm text-muted-foreground">Average Grade</p>
                  <p class="font-semibold text-lg">{{ advisoryInfo.avgGrade }}%</p>
                </div>
              </div>

              <div class="rounded-lg border p-4 flex items-center gap-3">
                <Clock class="h-6 w-6 text-orange-500" />
                <div>
                  <p class="text-sm text-muted-foreground">Adviser</p>
                  <p class="font-semibold text-lg">{{ advisoryInfo.adviser }}</p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Students Table -->
        <Card>
          <CardHeader>
            <CardTitle>Students List</CardTitle>
            <CardDescription>View and monitor student performance and attendance.</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="flex items-center justify-between mb-4">
              <Input v-model="search" placeholder="Search students..." class="max-w-xs" />
              <Button>
                <ChevronRight class="h-4 w-4 mr-2" />
                Export List
              </Button>
            </div>

            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student</TableHead>
                  <TableHead>Gender</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead>Grade</TableHead>
                  <TableHead class="text-right">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="student in students"
                  :key="student.id"
                  class="hover:bg-muted/50"
                >
                  <TableCell>
                    <span class="font-medium">{{ student.name }}</span>
                  </TableCell>

                  <TableCell class="text-muted-foreground">
                    {{ student.gender }}
                  </TableCell>

                  <TableCell>
                    <Badge :variant="
                      student.status === 'Present' ? 'default' :
                      student.status === 'Absent' ? 'destructive' : 'secondary'
                    ">
                      {{ student.status }}
                    </Badge>
                  </TableCell>

                  <TableCell class="font-semibold">{{ student.grade }}%</TableCell>

                  <TableCell class="text-right">
                    <Button variant="outline" size="sm">View</Button>
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
