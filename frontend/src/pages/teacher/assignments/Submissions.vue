<script lang="ts">
export const description = "Teacher assignment submissions page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed } from "vue"
import { useRoute, useRouter } from "vue-router"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
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
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
  SelectValue,
} from "@/components/ui/select"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  FileText,
  UserCheck,
  Clock4,
  CheckCircle2,
  File,
} from "lucide-vue-next"

const userRole = "Teacher"
const route = useRoute()
const router = useRouter()

const assignmentId = route.params.id ?? 1

// Filters
const statusFilter = ref("")
const search = ref("")

// Dummy submissions data
const submissions = ref([
  {
    id: 1,
    student: "Samantha Cruz",
    section: "STEM 11 - A",
    submittedAt: "2025-02-13 10:42 AM",
    status: "Submitted",
    score: null,
  },
  {
    id: 2,
    student: "Elijah Montes",
    section: "STEM 11 - A",
    submittedAt: null,
    status: "Missing",
    score: null,
  },
  {
    id: 3,
    student: "Marjorie Tan",
    section: "HUMSS 12 - B",
    submittedAt: "2025-02-14 1:15 PM",
    status: "Submitted",
    score: 95,
  },
  {
    id: 4,
    student: "Joshua Ramirez",
    section: "ABM 12 - A",
    submittedAt: "2025-02-14 2:04 PM",
    status: "Late",
    score: null,
  },
])

const filteredSubmissions = computed(() => {
  return submissions.value.filter((s) => {
    const matchStatus = statusFilter.value ? s.status === statusFilter.value : true
    const matchSearch = search.value
      ? s.student.toLowerCase().includes(search.value.toLowerCase())
      : true

    return matchStatus && matchSearch
  })
})
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
              <BreadcrumbLink href="/teacher/assignments">Assignments</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Submissions</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Assignment Submissions</h2>
            <p class="text-sm text-muted-foreground">
              View student submissions, grading status, and performance insights.
            </p>
          </div>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Total Students</CardTitle>
              <File class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">{{ submissions.length }}</p>
              <p class="text-xs text-muted-foreground mt-1">Expected to submit</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Submitted</CardTitle>
              <UserCheck class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{
                  submissions.filter((s) => s.status === "Submitted").length
                }}
              </p>
              <p class="text-xs text-muted-foreground mt-1">On time</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Late</CardTitle>
              <Clock4 class="h-5 w-5 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ submissions.filter((s) => s.status === "Late").length }}
              </p>
              <p class="text-xs text-muted-foreground mt-1">Submitted after deadline</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-red-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Missing</CardTitle>
              <FileText class="h-5 w-5 text-red-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ submissions.filter((s) => s.status === "Missing").length }}
              </p>
              <p class="text-xs text-muted-foreground mt-1">No submission</p>
            </CardContent>
          </Card>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Filters</CardTitle>
            <CardDescription>Filter submissions by name or status</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Status -->
              <Select v-model="statusFilter">
                <SelectTrigger>
                  <SelectValue placeholder="Select Status" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Submitted">Submitted</SelectItem>
                  <SelectItem value="Late">Late</SelectItem>
                  <SelectItem value="Missing">Missing</SelectItem>
                </SelectContent>
              </Select>

              <!-- Search -->
              <Input v-model="search" placeholder="Search student..." />
            </div>
          </CardContent>
        </Card>

        <!-- Submissions Table -->
        <Card>
          <CardHeader>
            <CardTitle>Student Submissions</CardTitle>
            <CardDescription>
              Click a row to view or grade the student's submission.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Name</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-center">Submitted At</TableHead>
                  <TableHead class="text-center">Score</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="s in filteredSubmissions"
                  :key="s.id"
                  class="hover:bg-muted/50 cursor-pointer"
                  @click="$router.push(`/teacher/assignments/${assignmentId}/submissions/${s.id}`)"
                >
                  <TableCell class="font-medium">
                    {{ s.student }}
                  </TableCell>

                  <TableCell>{{ s.section }}</TableCell>

                  <TableCell>
                    <Badge
                      :variant="
                        s.status === 'Submitted'
                          ? 'default'
                          : s.status === 'Late'
                          ? 'secondary'
                          : 'destructive'
                      "
                    >
                      {{ s.status }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-center">
                    {{ s.submittedAt ?? "—" }}
                  </TableCell>

                  <TableCell class="text-center font-semibold">
                    {{ s.score ?? "—" }}
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
